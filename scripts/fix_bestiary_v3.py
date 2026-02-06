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

# Match from <div class="stat-block"> until a </div> that is on its own line (or at least starts at the beginning of the line in the original, but we already stripped some)
# A better way: match until the </div> that closes the stat-block. 
# Given my previous edits, the closing </div> is always followed by \n\n or end of file.
fixed = re.sub(r'<div class="stat-block">.*?</div>\n(?=\n|$)', clean_stat_block, content, flags=re.DOTALL)

with open('Bestiary.md', 'w') as f:
    f.write(fixed)
