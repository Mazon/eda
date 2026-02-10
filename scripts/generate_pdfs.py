import subprocess
import os
import shutil

def convert_md_to_pdf(input_file, output_file, css_file=None, title=None):
    print(f"Converting {input_file} to {output_file}...")
    try:
        # Use pandoc to convert to HTML first
        html_file = input_file.replace('.md', '.html')
        print(f"  Generating intermediate HTML: {html_file}")
        
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

        # Now use md-to-pdf (which uses Puppeteer) to convert the HTML to PDF
        # It handles HTML inputs well and renders them as they would appear in a browser
        md_to_pdf_path = shutil.which('md-to-pdf')
        if not md_to_pdf_path:
            potential_paths = [
                '/usr/local/bin/md-to-pdf',
                '/opt/homebrew/bin/md-to-pdf',
                os.path.expanduser('~/.npm-global/bin/md-to-pdf')
            ]
            for p in potential_paths:
                if os.path.exists(p):
                    md_to_pdf_path = p
                    break

        if md_to_pdf_path:
            # Build pdf-options based on file type
            pdf_options = '{"format": "A4", "margin": {"top": "15mm", "right": "15mm", "bottom": "15mm", "left": "15mm"}, "printBackground": true}'
            if input_file in ['Character Sheet.md', 'Cheat_Sheet.md']:
                # Use smaller margins for sheets to fit everything
                pdf_options = '{"format": "A4", "margin": {"top": "0", "right": "0", "bottom": "0", "left": "0"}, "printBackground": true}'
            
            # Additional options to ensure local file access if needed
            # But md-to-pdf generally handles local files fine

            subprocess.run([
                md_to_pdf_path,
                html_file,
                '--pdf-options', pdf_options
            ], check=True)

            # md-to-pdf creates pdf in same dir with .pdf extension
            temp_output = html_file.replace('.html', '.pdf')
            if os.path.exists(temp_output):
                shutil.move(temp_output, output_file)
                print(f"Successfully created {output_file}")
            else:
                print(f"Error: Expected output {temp_output} not found.")
        else:
            print("md-to-pdf not found, cannot complete high-quality conversion.")

        # Cleanup intermediate HTML
        if os.path.exists(html_file):
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

    # List of files to convert: { markdown_file: (pdf_name, title) }
    files_to_convert = {
        'Core Rulebook.md': ('Core_Rulebook.pdf', 'Eda Core Rulebook'),
        'Bestiary.md': ('Bestiary.pdf', 'Eda Bestiary'),
        'Character Sheet.md': ('Character_Sheet.pdf', None),
        'Cheat_Sheet.md': ('Cheat_Sheet.pdf', None),
        'Adventure_The_Age_of_Wolves.md': ('Adventure_The_Age_of_Wolves.pdf', 'The Age of Wolves')
    }

    style_css = 'scripts/style.css'

    for md_file, (pdf_file, title) in files_to_convert.items():
        if os.path.exists(md_file):
            output_path = os.path.join(build_dir, pdf_file)
            
            # Apply CSS to all except Sheets (they have embedded styles)
            current_css = style_css if md_file not in ['Character Sheet.md', 'Cheat_Sheet.md'] else None
            
            convert_md_to_pdf(md_file, output_path, css_file=current_css, title=title)
        else:
            print(f"Warning: {md_file} not found, skipping.")

if __name__ == "__main__":
    main()
