import re

with open('Bestiary.md', 'r') as f:
    content = f.read()

def clean_html_block(match):
    block_content = match.group(0)
    # Split the block into lines, remove leading/trailing whitespace from each line
    lines = [line.strip() for line in block_content.splitlines()]
    # Filter out empty lines within the block
    cleaned_lines = [line for line in lines if line]
    return '\n'.join(cleaned_lines)

# This regex captures the entire stat-block div, including its content
# The (?:\s*\n\s*){2,} ensures at least two blank lines follow a div for separation,
# but we only use it for parsing, not for modifying blank lines outside the blocks.
fixed_content = re.sub(r'(<div class="stat-block">.*?</div>)(?:\s*\n\s*){0,}', clean_html_block, content, flags=re.DOTALL)

# Now, let's explicitly handle spacing between blocks and after headers
# Ensure exactly two newlines between blocks
fixed_content = re.sub(r'</div>\s*<div class="stat-block">', '</div>\n\n<div class="stat-block">', fixed_content)

# Ensure exactly two newlines after headers before the first stat block or next section
fixed_content = re.sub(r'(## .*?)\n\n+(<div class="stat-block">)', r'\1\n\n\2', fixed_content)
fixed_content = re.sub(r'(---)\n\n+(## .*?)\n\n+(<div class="stat-block">)', r'\1\n\n\2\n\n\3', fixed_content)
fixed_content = re.sub(r'(---)\n\n+(## .*?)\n\n+(# .*?)\n\n+(<div class="stat-block">)', r'\1\n\n\2\n\n\3\n\n\4', fixed_content)

# Remove any extra blank lines that might have been introduced or remained globally (more than 2 consecutive newlines)
fixed_content = re.sub(r'\n{3,}', '\n\n', fixed_content)

with open('Bestiary.md', 'w') as f:
    f.write(fixed_content)
