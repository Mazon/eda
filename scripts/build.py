import subprocess
import os
import shutil

def run_command(command):
    """Runs a command and prints errors if they occur."""
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        print(f"Stderr: {e.stderr}")
        return False

def convert_md_to_html(input_file, output_file, css_file=None):
    """Converts a Markdown file to HTML using Pandoc."""
    print(f"Converting {input_file} to {output_file} with Pandoc...")
    
    # Check if file has <style> tags - if so, it's likely a mix of HTML and MD
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Detect if the file is basically an HTML document disguised as Markdown
    is_pure_html = '<style>' in content and '<div class="page">' in content
    
    if is_pure_html:
        # Just copy it, Pandoc ruins these files even with +raw_html
        shutil.copy(input_file, output_file)
        return True

    command = [
        'pandoc',
        input_file,
        '-s', # standalone
        '-f', 'markdown+raw_html',
        '-t', 'html',
        '-o', output_file
    ]
    if css_file:
        command.extend(['--css', css_file])
    return run_command(command)

def convert_with_weasyprint(input_file, output_file):
    """Converts an HTML file to PDF using WeasyPrint."""
    print(f"Converting {input_file} to {output_file} with WeasyPrint...")
    weasyprint_path = shutil.which('weasyprint')
    if not weasyprint_path:
        potential_paths = [
            '/usr/local/bin/weasyprint',
            '/opt/homebrew/bin/weasyprint',
            os.path.expanduser('~/.local/bin/weasyprint')
        ]
        for p in potential_paths:
            if os.path.exists(p):
                weasyprint_path = p
                break
    
    if weasyprint_path:
        if run_command([weasyprint_path, input_file, output_file]):
            print(f"Successfully created {output_file}")
            return True
    else:
        print("Error: weasyprint not found. Please install it with 'pip install weasyprint'.")
    
    return False

def main():
    """Main build process."""
    build_dir = 'build'
    scripts_dir = 'scripts'
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
        
    cleanup_files = []

    # --- 1. Character Sheet (HTML -> PDF) ---
    print("--- Processing Character Sheet ---")
    char_sheet_html_in = 'character_sheet.html'
    if os.path.exists(char_sheet_html_in):
        # First, prepare the interactive HTML
        char_sheet_html_interactive = 'character_sheet_interactive.html'
        print("  Generating interactive HTML version...")
        if run_command(['python3', 'scripts/prepare_html.py']):
            char_sheet_pdf_out = os.path.join(build_dir, 'Character_Sheet.pdf')
            # WeasyPrint requires specific CSS for interactive forms (appearance: none + border)
            # or it might just render them as static. 
            # Let's try to run it.
            if not convert_with_weasyprint(char_sheet_html_interactive, char_sheet_pdf_out):
                print("Character Sheet generation failed.")
            cleanup_files.append(char_sheet_html_interactive)
        else:
            print("Failed to prepare interactive HTML.")
    else:
        print(f"Warning: {char_sheet_html_in} not found.")

    # --- 2. Cheat Sheet (MD -> HTML -> PDF) ---
    print("\n--- Processing Cheat Sheet ---")
    cheat_sheet_md = 'Cheat_Sheet.md'
    if os.path.exists(cheat_sheet_md):
        cheat_sheet_html = 'cheat_sheet.html'
        cheat_sheet_pdf = os.path.join(build_dir, 'Cheat_Sheet.pdf')
        cleanup_files.append(cheat_sheet_html)
        
        # Convert MD to HTML, preserving styles inside
        if convert_md_to_html(cheat_sheet_md, cheat_sheet_html):
            if not convert_with_weasyprint(cheat_sheet_html, cheat_sheet_pdf):
                print("Cheat Sheet generation failed.")
    else:
        print(f"Warning: {cheat_sheet_md} not found.")

    # --- 3. Other Markdown Files ---
    print("\n--- Processing Other Documents ---")
    style_css = os.path.join(scripts_dir, 'style.css')
    other_files = {
        'Core Rulebook.md': 'Core_Rulebook.pdf',
        'Bestiary.md': 'Bestiary.pdf',
        'Adventure_The_Age_of_Wolves.md': 'Adventure_The_Age_of_Wolves.pdf'
    }

    for md_file, pdf_file in other_files.items():
        if os.path.exists(md_file):
            temp_html = md_file.replace('.md', '.html')
            output_pdf = os.path.join(build_dir, pdf_file)
            cleanup_files.append(temp_html)
            
            print(f"\nProcessing {md_file}...")
            if convert_md_to_html(md_file, temp_html, css_file=style_css):
                if not convert_with_weasyprint(temp_html, output_pdf):
                    print(f"Failed to generate PDF for {md_file}.")
        else:
            print(f"Warning: {md_file} not found, skipping.")

    # --- Cleanup ---
    print("\n--- Cleaning up intermediate files ---")
    for f in cleanup_files:
        if os.path.exists(f):
            os.remove(f)
            print(f"Removed {f}")
            
    print("\nBuild process complete.")

if __name__ == "__main__":
    main()
