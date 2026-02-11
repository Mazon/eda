import subprocess
import os
import shutil
import sys

def convert_md_to_pdf(input_file, output_file, css_file=None, title=None):
    """
    Converts a Markdown file to PDF using Pandoc and WeasyPrint.
    This avoids dependencies on Node.js and Chromium.
    """
    print(f"Converting {input_file} to {output_file}...")
    try:
        # Check if the input is actually HTML
        is_html = input_file.lower().endswith('.html')
        
        if is_html:
            html_file = input_file
            print(f"  Using existing HTML: {html_file}")
        else:
            # Use pandoc to convert to HTML first
            html_file = input_file.replace('.md', '.html')
            print(f"  Generating intermediate HTML from Markdown: {html_file}")
            
            pandoc_args = [
                'pandoc',
                input_file,
                '-s', # standalone
                '-f', 'markdown+raw_html', # ensure HTML is preserved
                '--toc', # Generate Table of Contents
                '-o', html_file
            ]

            if title:
                pandoc_args.extend(['--metadata', f'title={title}'])

            if css_file:
                 pandoc_args.extend(['--css', css_file])

            subprocess.run(pandoc_args, check=True)

        # Now use weasyprint to convert the HTML to PDF
        # Use sys.executable to ensure we use the same python interpreter
        print(f"  Running WeasyPrint on {html_file}...")
        subprocess.run([
            sys.executable, '-m', 'weasyprint',
            html_file,
            output_file
        ], check=True)

        print(f"Successfully created {output_file}")

        # Cleanup intermediate HTML (only if it was generated from .md)
        if not is_html and os.path.exists(html_file):
            os.remove(html_file)
            
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ensure build directory exists
    build_dir = 'build'
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    # List of files to convert: { source_file: (pdf_name, title) }
    # We now use the .html versions for the sheets to avoid Pandoc escaping
    files_to_convert = {
        'Core Rulebook.md': ('Core_Rulebook.pdf', 'Eda Core Rulebook'),
        'Creature_Compendium.md': ('Creature_Compendium.pdf', 'Eda Creature Compendium'),
        'character_sheet.html': ('Character_Sheet.pdf', None),
        'Cheat_Sheet.md': ('Cheat_Sheet.pdf', None),
        'Adventure_The_Age_of_Wolves.md': ('Adventure_The_Age_of_Wolves.pdf', 'The Age of Wolves'),
        'World_of_Eda.md': ('World_of_Eda.pdf', 'World of Eda')
    }

    style_css = 'scripts/style.css'

    for md_file, (pdf_file, title) in files_to_convert.items():
        if os.path.exists(md_file):
            output_path = os.path.join(build_dir, pdf_file)
            
            # Apply CSS to all except Sheets (they have embedded styles or complex layout)
            # Note: WeasyPrint might struggle with complex CSS/JS-heavy layouts that Puppeteer handled,
            # but for standard Markdown-derived HTML it works great.
            current_css = style_css if md_file not in ['Character Sheet.md', 'Cheat_Sheet.md'] else None
            
            convert_md_to_pdf(md_file, output_path, css_file=current_css, title=title)
        else:
            print(f"Warning: {md_file} not found, skipping.")

if __name__ == "__main__":
    main()
