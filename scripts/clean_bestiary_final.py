import re

def clean_bestiary_md(file_path="Bestiary.md"):
    with open(file_path, "r") as f:
        lines = f.readlines()

    output_lines = []
    div_depth = 0
    in_stat_block = False
    for line in lines:
        # Count depth changes in this line
        open_divs = line.count("<div")
        close_divs = line.count("</div>")
        
        # Check if entering stat block
        if "<div class=\"stat-block\">" in line:
            in_stat_block = True
        
        if in_stat_block:
            div_depth += open_divs - close_divs
            
            # Remove all whitespace from lines within a stat block
            stripped_line = line.strip()
            if stripped_line:
                output_lines.append(stripped_line)
            
            # check if we exited
            if div_depth <= 0:
                in_stat_block = False
                div_depth = 0 # reset to be safe
        else:
            # For lines outside a stat block, keep only significant lines
            stripped_line = line.strip()
            if stripped_line:
                output_lines.append(stripped_line)
            elif output_lines and output_lines[-1] != ":": # Allow single blank line, but not if previous was a list item description separator
                output_lines.append("")

    # Join the lines and then normalize blank lines globally
    cleaned_content = "\n".join(output_lines)
    # Replace three or more newlines with exactly two newlines, to ensure proper paragraph breaks
    cleaned_content = re.sub(r"\n{3,}", "\n\n", cleaned_content)

    with open(file_path, "w") as f:
        f.write(cleaned_content)

clean_bestiary_md()
