import re
with open('Bestiary.md', 'r') as f:
    content = f.read()

# Remove all leading whitespace and sequences of newlines
def aggressive_clean(text):
    # Remove all leading whitespace from each line
    text = re.sub(r'^[ \t]+', '', text, flags=re.MULTILINE)
    # Remove empty lines (including those with whitespace)
    lines = [line for line in text.splitlines() if line.strip()]
    return '\n'.join(lines)

# Split by the start of each stat block
parts = re.split(r'(<div class="stat-block">)', content)
# parts[0] is preamble
# parts[1] is '<div class="stat-block">'
# parts[2] is the content of the first block... up to next match

new_parts = [parts[0]]
for i in range(1, len(parts), 2):
    tag = parts[i]
    rest = parts[i+1]
    
    # In rest, we need to find the closing </div> of the stat-block
    # Since stat-blocks are not nested, it's the </div> that doesn't have a matching <div> before it.
    # But wait, we have nested divs inside.
    # We can find the closing </div> by looking for the one followed by \n\n or end of string.
    
    match = re.search(r'(.*?)</div>(\s*\n\s*\n|\s*$)', rest, flags=re.DOTALL)
    if match:
        block_content = match.group(1)
        after = rest[match.end():]
        
        cleaned = aggressive_clean(tag + block_content + "</div>")
        new_parts.append(cleaned)
        new_parts.append("\n\n" + after)
    else:
        new_parts.append(tag + rest)

with open('Bestiary.md', 'w') as f:
    f.write("".join(new_parts))
