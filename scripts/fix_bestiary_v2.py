import re
with open('Bestiary.md', 'r') as f:
    content = f.read()

def clean_stat_block(match):
    block = match.group(0)
    # Remove all leading whitespace on each line
    lines = [line.strip() for line in block.splitlines()]
    # Remove empty lines
    lines = [line for line in lines if line]
    # Join with single newline
    return "\n".join(lines)

# Non-greedy match for stat-block divs
fixed = re.sub(r'<div class="stat-block">.*?</div>', clean_stat_block, content, flags=re.DOTALL)

# Ensure double newlines between blocks
fixed = re.sub(r'</div>\s*<div', '</div>\n\n<div', fixed)

with open('Bestiary.md', 'w') as f:
    f.write(fixed)
