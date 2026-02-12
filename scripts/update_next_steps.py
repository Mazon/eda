#!/usr/bin/env python3
"""Update Next Steps section in implementation_summary.md"""

def update_next_steps():
    """Update Next Steps section to remove steps 2,3,4,5 and keep step1 as done."""
    
    with open('plans/implementation_summary.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the Next Steps section
    old_section = """---

## Next Steps

1. **Test build system** - Run `python scripts/build.py` to verify all PDFs generate correctly
2. **Create content creation plan** for World of Eda placeholder sections
3. **Decide on heritage/archetype system** - Choose one approach from conflicting plans
4. **Set up automated testing** - Create test suite for game mechanics
5. **Implement CI/CD** - Set up GitHub Actions for automated builds and testing

---

## Conclusion"""
    
    new_section = """---

## Next Steps

1. **Begin content creation** - Use [`plans/world_of_eda_content_plan.md`](world_of_eda_content_plan.md) to start writing World of Eda placeholder sections
2. **Decide on heritage/archetype system** - Choose one approach from conflicting plans
3. **Set up automated testing** - Create test suite for game mechanics
4. **Implement CI/CD** - Set up GitHub Actions for automated builds and testing

---

## Conclusion"""
    
    content = content.replace(old_section, new_section)
    
    with open('plans/implementation_summary.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated Next Steps section in implementation_summary.md")

if __name__ == "__main__":
    update_next_steps()
