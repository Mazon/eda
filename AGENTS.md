# Agent Instructions for Project Eda

To maintain consistency and ensure successful builds in this project, all AI agents should adhere to the following rules:

## 1. Environment Management
- **Always** run Python scripts within a virtual environment (`venv`).
- Ensure dependencies from `requirements.txt` are installed in the `venv`.
- Use `source venv/bin/activate` before executing scripts like `generate_pdfs_weasy.py`.

## 2. Text Formatting (Core Rulebook & World Docs)
- **Bold Text**: Use bolding **only when really neccessary**. Focus on core game mechanics when first introduced or critical numerical values. Do not over-bold descriptive or flavor text.
- **Capitalization**: Use capital letters **only when really needed**. Typically for Attribute names (e.g., **STR**, **AGI**), Skill names (e.g., **Athletics**), and proper nouns. Avoid unnecessary capitalization for emphasis.

## 3. Layout & Media
- **Heritages**: Use the `two-column-layout` div for Heritage introductions.
    - One column should contain the Heritage image and flavor text.
    - The other column should contain the trait, skills, and starting gear.
- **Tables**: Tables must always be full page width. Do not place them inside multi-column layouts.
- **Headings**: Ensure "X Talents" sections are real Markdown headings (e.g., `####`).
- **Missing Images**: If an image is missing, use `images/placeholder.png` rather than leaving a broken link or using an incorrect image.
- **Clearing Floats**: Always use `<div class="clearfix"></div>` after sections with floated elements to prevent layout bleeding.
