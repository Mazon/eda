import re

with open("Bestiary.md", "r") as f:
    content = f.read()

def remove_h3_numbering(match):
    h3_tag_content = match.group(1)
    # Remove the "NUMBER. " prefix from the content within <h3>
    cleaned_h3_content = re.sub(r"^\d+\.\s*", "", h3_tag_content)
    return f"<h3>{cleaned_h3_content}</h3>"

# Regex to find <h3> tags within a div with class "stat-block"
# It specifically looks for the pattern inside the <h3> tag.
fixed_content = re.sub(r"<h3>(.*?)</h3>", lambda m: f"<h3>{re.sub(r'^\d+\.\s*', '', m.group(1))}</h3>", content, flags=re.DOTALL)

with open("Bestiary.md", "w") as f:
    f.write(fixed_content)
