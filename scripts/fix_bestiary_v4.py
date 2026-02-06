import re
with open('Bestiary.md', 'r') as f:
    content = f.read()

# Remove all blank lines and indentation from stat-blocks
def final_clean(match):
    block = match.group(0)
    # Remove all leading whitespace
    block = re.sub(r'^[ \t]+', '', block, flags=re.MULTILINE)
    # Replace all sequences of 2 or more newlines with a single newline
    block = re.sub(r'\n\s*\n+', '\n', block)
    return block

# Find stat blocks. They start with <div class="stat-block"> and end with </div>
# Since they are NOT nested (stat-block itself isn't nested), we can match non-greedily to the NEXT </div> 
# that is at the start of a line (after we strip). 
# Actually, let's just use the fact that they end with "</div>\n" and are followed by another div or header.

# This regex matches from <div class="stat-block"> to the </div> that is followed by a blank line or end of file.
fixed = re.sub(r'<div class="stat-block">.*?</div>', final_clean, content, flags=re.DOTALL)

# Now fix the spacing between blocks
fixed = re.sub(r'</div>\n<div', '</div>\n\n<div', fixed)

with open('Bestiary.md', 'w') as f:
    f.write(fixed)
