#!/usr/bin/env python3
"""
Eda TTRPG Build Script
Consolidated build script for generating all PDFs from Markdown and HTML sources.
Uses Pandoc and WeasyPrint (no Node.js dependency required).
"""

import subprocess
import os
import shutil
import sys
import time
from pathlib import Path

# Configuration
BUILD_DIR = 'build'
SCRIPTS_DIR = 'scripts'
STYLE_CSS = os.path.join(SCRIPTS_DIR, 'style.css')

# Files to convert: { source_file: (pdf_name, title, use_css, is_html) }
FILES_TO_CONVERT = {
    'Core Rulebook.md': ('Core_Rulebook.pdf', 'Eda Core Rulebook', True, False),
    'Creature_Compendium.md': ('Creature_Compendium.pdf', 'Eda Creature Compendium', True, False),
    'Cheat_Sheet.md': ('Cheat_Sheet.pdf', None, False, True),  # HTML file with .md extension
    'Adventure_The_Age_of_Wolves.md': ('Adventure_The_Age_of_Wolves.pdf', 'The Age of Wolves', True, False),
    'World_of_Eda.md': ('World_of_Eda.pdf', 'World of Eda', True, False),
    'character_sheet.html': ('Character_Sheet.pdf', None, False, True),
}


def log(message, level='INFO'):
    """Print formatted log message."""
    timestamp = time.strftime('%H:%M:%S')
    print(f'[{timestamp}] [{level}] {message}')


def check_venv():
    """Check if running in virtual environment."""
    venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'venv')
    
    # Check if VIRTUAL_ENV is set (Unix-like systems)
    if 'VIRTUAL_ENV' in os.environ:
        return True
    
    # Check if we're running from venv/bin/python (common on Unix)
    if 'venv' in sys.prefix or 'venv' in sys.executable:
        return True
    
    # Check if venv directory exists
    if os.path.exists(venv_path):
        log("WARNING: Virtual environment exists but not activated.", 'WARNING')
        log(f"To activate: source {venv_path}/bin/activate", 'INFO')
        return False
    
    log("WARNING: No virtual environment found.", 'WARNING')
    log("Create one with: python3 -m venv venv", 'INFO')
    log("Then activate with: source venv/bin/activate", 'INFO')
    return False


def run_command(command, check=True, capture_output=False):
    """
    Run a command and return success status.
    
    Args:
        command: List of command arguments
        check: If True, raise exception on failure
        capture_output: If True, capture stdout/stderr
    
    Returns:
        True if successful, False otherwise
    """
    try:
        result = subprocess.run(
            command,
            check=check,
            capture_output=capture_output,
            text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        log(f"Command failed: {' '.join(command)}", 'ERROR')
        if capture_output and e.stderr:
            log(f"Stderr: {e.stderr}", 'ERROR')
        return False
    except FileNotFoundError:
        log(f"Command not found: {command[0]}", 'ERROR')
        return False


def find_weasyprint():
    """Find WeasyPrint executable in common locations."""
    weasyprint_path = shutil.which('weasyprint')
    
    if weasyprint_path:
        return weasyprint_path
    
    # Check common installation paths
    potential_paths = [
        '/usr/local/bin/weasyprint',
        '/opt/homebrew/bin/weasyprint',
        os.path.expanduser('~/.local/bin/weasyprint'),
    ]
    
    for path in potential_paths:
        if os.path.exists(path):
            return path
    
    return None


def check_dependencies():
    """Check if required dependencies are installed."""
    log("Checking dependencies...")
    
    # Check Python
    if sys.version_info < (3, 10):
        log(f"Python 3.10+ required, found {sys.version}", 'ERROR')
        return False
    
    # Check Pandoc
    if not shutil.which('pandoc'):
        log("Pandoc not found. Please install from https://pandoc.org/", 'ERROR')
        return False
    log("✓ Pandoc found")
    
    # Check WeasyPrint
    weasyprint_path = find_weasyprint()
    if not weasyprint_path:
        log("WeasyPrint not found. Install with: pip install weasyprint", 'ERROR')
        return False
    log("✓ WeasyPrint found")
    
    return True


def convert_md_to_html(input_file, output_file, css_file=None, title=None):
    """
    Convert a Markdown file to HTML using Pandoc.
    
    Args:
        input_file: Path to input Markdown file
        output_file: Path to output HTML file
        css_file: Optional path to CSS file
        title: Optional title metadata
    
    Returns:
        True if successful, False otherwise
    """
    log(f"Converting {input_file} to HTML...")
    
    # Check if file is actually HTML (for character sheet)
    if input_file.lower().endswith('.html'):
        log(f"  File is already HTML, copying...")
        try:
            shutil.copy(input_file, output_file)
            return True
        except Exception as e:
            log(f"  Failed to copy: {e}", 'ERROR')
            return False
    
    # Build Pandoc command
    command = [
        'pandoc',
        input_file,
        '-s',  # standalone
        '-f', 'markdown+raw_html',  # preserve HTML
        '-t', 'html',
        '--toc',  # Generate Table of Contents
        '-o', output_file
    ]
    
    if title:
        command.extend(['--metadata', f'title={title}'])
    
    if css_file:
        command.extend(['--css', css_file])
    
    return run_command(command)


def convert_html_to_pdf(input_file, output_file):
    """
    Convert an HTML file to PDF using WeasyPrint.
    
    Args:
        input_file: Path to input HTML file
        output_file: Path to output PDF file
    
    Returns:
        True if successful, False otherwise
    """
    log(f"Converting {input_file} to PDF...")
    
    weasyprint_path = find_weasyprint()
    if not weasyprint_path:
        log("WeasyPrint not found!", 'ERROR')
        return False
    
    # Use Python module to run WeasyPrint
    command = [sys.executable, '-m', 'weasyprint', input_file, output_file]
    
    return run_command(command)


def prepare_character_sheet():
    """
    Prepare the interactive character sheet HTML.
    
    Returns:
        Path to prepared HTML file, or None if failed
    """
    log("Preparing interactive character sheet...")
    
    prepare_script = os.path.join(SCRIPTS_DIR, 'prepare_html.py')
    if not os.path.exists(prepare_script):
        log(f"Prepare script not found: {prepare_script}", 'WARNING')
        return 'character_sheet.html'
    
    if not run_command(['python3', prepare_script]):
        log("Failed to prepare interactive HTML", 'WARNING')
        return 'character_sheet.html'
    
    interactive_file = 'character_sheet_interactive.html'
    if os.path.exists(interactive_file):
        return interactive_file
    
    return 'character_sheet.html'


def build_all():
    """Build all PDFs."""
    start_time = time.time()
    
    log("=" * 60)
    log("Eda TTRPG Build System")
    log("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        log("\nBuild failed: Missing dependencies", 'ERROR')
        return False
    
    # Create build directory
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)
        log(f"Created build directory: {BUILD_DIR}")
    
    # Track intermediate files for cleanup
    cleanup_files = []
    success_count = 0
    total_count = len(FILES_TO_CONVERT)
    
    # Process each file
    for i, (source_file, (pdf_name, title, use_css, is_html)) in enumerate(FILES_TO_CONVERT.items(), 1):
        log(f"\n[{i}/{total_count}] Processing: {source_file}")
        
        if not os.path.exists(source_file):
            log(f"  File not found, skipping...", 'WARNING')
            continue
        
        # Determine input file (for character sheet, prepare it first)
        input_file = source_file
        if source_file == 'character_sheet.html':
            input_file = prepare_character_sheet()
            if input_file != source_file:
                cleanup_files.append(input_file)
        
        # Generate intermediate HTML
        html_file = source_file.rsplit('.', 1)[0] + '.html'
        
        # For HTML files, use the file directly
        if is_html or source_file.lower().endswith('.html'):
            html_file = source_file
        else:
            cleanup_files.append(html_file)
        
        # Convert to HTML (skip if already HTML)
        css_file = STYLE_CSS if use_css else None
        if not is_html and not source_file.lower().endswith('.html'):
            if not convert_md_to_html(input_file, html_file, css_file, title):
                log(f"  Failed to convert to HTML", 'ERROR')
                continue
        
        # Convert to PDF
        output_pdf = os.path.join(BUILD_DIR, pdf_name)
        if convert_html_to_pdf(html_file, output_pdf):
            log(f"  ✓ Created: {output_pdf}")
            success_count += 1
        else:
            log(f"  Failed to create PDF", 'ERROR')
    
    # Cleanup intermediate files
    log("\n" + "-" * 60)
    log("Cleaning up intermediate files...")
    for f in cleanup_files:
        if os.path.exists(f) and f != 'character_sheet.html':
            try:
                os.remove(f)
                log(f"  Removed: {f}")
            except Exception as e:
                log(f"  Failed to remove {f}: {e}", 'WARNING')
    
    # Summary
    elapsed = time.time() - start_time
    log("\n" + "=" * 60)
    log("Build Summary")
    log("=" * 60)
    log(f"Successfully built: {success_count}/{total_count} files")
    log(f"Time elapsed: {elapsed:.2f} seconds")
    log(f"Output directory: {os.path.abspath(BUILD_DIR)}")
    
    if success_count == total_count:
        log("\n✓ All files built successfully!")
        return True
    else:
        log(f"\n⚠ {total_count - success_count} file(s) failed to build", 'WARNING')
        return False


def build_specific(filename):
    """Build a specific PDF file."""
    log(f"Building specific file: {filename}")
    
    # Find matching file in FILES_TO_CONVERT
    for source_file, (pdf_name, title, use_css, is_html) in FILES_TO_CONVERT.items():
        if source_file == filename or pdf_name == filename:
            if not os.path.exists(source_file):
                log(f"File not found: {source_file}", 'ERROR')
                return False
            
            # Create build directory
            if not os.path.exists(BUILD_DIR):
                os.makedirs(BUILD_DIR)
            
            # Convert
            html_file = source_file.rsplit('.', 1)[0] + '.html'
            css_file = STYLE_CSS if use_css else None
            
            # Skip Pandoc conversion for HTML files
            if not is_html and not source_file.lower().endswith('.html'):
                if not convert_md_to_html(source_file, html_file, css_file, title):
                    log("Failed to convert to HTML", 'ERROR')
                    return False
            else:
                html_file = source_file
            
            output_pdf = os.path.join(BUILD_DIR, pdf_name)
            if convert_html_to_pdf(html_file, output_pdf):
                log(f"✓ Created: {output_pdf}")
                # Cleanup
                if os.path.exists(html_file) and html_file != source_file:
                    os.remove(html_file)
                return True
            else:
                log("Failed to create PDF", 'ERROR')
                return False
    
    log(f"File not found in build list: {filename}", 'ERROR')
    return False


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Build Eda TTRPG PDFs from Markdown and HTML sources.'
    )
    parser.add_argument(
        'file',
        nargs='?',
        help='Specific file to build (e.g., "Core Rulebook.md" or "Core_Rulebook.pdf")'
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='Check dependencies only'
    )
    
    args = parser.parse_args()
    
    # Check if running in virtual environment
    if not args.check:  # Skip venv check for --check flag
        check_venv()
    
    if args.check:
        success = check_dependencies()
        sys.exit(0 if success else 1)
    
    if args.file:
        success = build_specific(args.file)
    else:
        success = build_all()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
