import re

def main():
    """
    Converts the placeholder divs in character_sheet.html to actual form inputs
    that WeasyPrint can turn into interactive PDF fields.
    """
    input_path = 'character_sheet.html'
    output_path = 'character_sheet_interactive.html' # a new file to be safe

    try:
        with open(input_path, 'r') as f:
            content = f.read()

        # --- Text Inputs ---
        # Simple placeholders: <div class="input-field" data-field="some_name"></div>
        content = re.sub(
            r'<div class="input-field" data-field="([^"]+)"(.*?)></div>',
            r'<input type="text" name="\1" class="input-field" \2 />',
            content
        )
        
        # Table cell placeholders: <td><div class="input-field" data-field="some_name"></div></td>
        content = re.sub(
            r'<td><div class="input-field" data-field="([^"]+)"(.*?)></div></td>',
            r'<td><input type="text" name="\1" \2 /></td>',
            content
        )
        
        # Box inputs: <div class="box-input" data-field="some_name" ...></div>
        content = re.sub(
            r'<div class="box-input" data-field="([^"]+)"(.*?)></div>',
            r'<input type="text" name="\1" class="box-input" \2 />',
            content
        )

        # --- Text Areas ---
        # Multiline fields: <div ... data-multiline="true" ...></div>
        content = re.sub(
            r'<input type="text" name="([^"]+)" class="input-field" data-multiline="true"(.*?)/>',
            r'<textarea name="\1" class="input-field" \2></textarea>',
            content
        )

        # --- Checkboxes ---
        # Circle checkboxes: <div class="circle-checkbox" data-field="some_name" ...></div>
        content = re.sub(
            r'<div class="circle-checkbox" data-field="([^"]+)" data-type="checkbox"(.*?)></div>',
            r'<input type="checkbox" name="\1" class="circle-checkbox" \2 />',
            content
        )
        
        # Square checkboxes: <div class="square-checkbox" ...></div>
        content = re.sub(
            r'<div class="square-checkbox" data-field="([^"]+)" data-type="checkbox"(.*?)></div>',
            r'<input type="checkbox" name="\1" class="square-checkbox" \2 />',
            content
        )

        with open(output_path, 'w') as f:
            f.write(content)
            
        print(f"Successfully created interactive HTML at {output_path}")

    except FileNotFoundError:
        print(f"Error: {input_path} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
