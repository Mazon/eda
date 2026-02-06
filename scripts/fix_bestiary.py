import re

with open('Bestiary.md', 'r') as f:
    content = f.read()

def clean_block(match):
    block = match.group(0)
    # Remove all leading spaces from each line
    block = re.sub(r'^[ \t]+', '', block, flags=re.MULTILINE)
    # Remove empty lines within the block
    lines = [line for line in block.split('\n') if line.strip()]
    return '\n'.join(lines)

# Find all <div class="stat-block">...</div> blocks
fixed_content = re.sub(r'<div class="stat-block">.*?</div>', clean_block, content, flags=re.DOTALL)

# Ensure exactly two newlines between blocks
fixed_content = re.sub(r'</div>\s*<div', '</div>\n\n<div', fixed_content)

# Also ensure exactly one newline after headers before the first div
fixed_content = re.sub(r'## (.*?)\n\n<div', r'## \1\n\n<div', fixed_content)

with open('Bestiary.md', 'w') as f:
    f.write(fixed_content)
