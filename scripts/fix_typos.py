#!/usr/bin/env python3
"""
Script to fix typos in World_of_Eda.md
"""

import re

def fix_typos():
    """Fix typos in World_of_Eda.md"""
    
    # Read the file
    with open('World_of_Eda.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define replacements
    replacements = {
        # Grammar and spelling fixes
        "didn't": "didn't",
        "roughly": "roughly",
        "enlighten": "enlightened",
        "year423": "year 423",
        "roughtly": "roughly",
        "extenstion": "extinction",
        "i ssis": "i.e.,",
        "where": "who wear",
        "titans": "titans",
        "suns": "suns",
        "persitent": "persistent",
        "Titans": "Titans",
        "Cracked": "Cracked",
        "Existence": "Existence",
        "Demoner": "Demons",
        "Terrors": "Terrors",
        "Demonology": "Demonology",
        "Faiths": "Faiths",
        "Urgudar": "Urgudar",
        "Veiled": "Veiled",
        "impurity": "impurity",
        "Valerius": "Valerius",
        "Tyranny": "Tyranny",
        "Korint": "Korint",
        "cauterized": "cauterized",
        "citadels": "citadels",
        "Inquisitors": "Inquisitors",
        "Ashen": "Ashen",
        "clings": "clings",
        "Ever-Fires": "Ever-Fires",
        "encroaching": "encroaching",
        "Cults": "Cults",
        "Void-Worshippers": "Void-Worshippers",
        "hasten": "hasten",
        "Prosperity": "Prosperity",
        "giants": "giants",
        "spires": "spires",
        "thought-glass": "thought-glass",
        "harnessed": "harnessed",
        "frosts": "frosts",
        "Pustule": "Pustule",
        "ailment": "ailment",
        "etheric": "etheric",
        "Empires": "Empires",
        "Silent": "Silent",
        "rusted": "rusted",
        "coronation": "coronation",
        "Oakhaven": "Oakhaven",
        "Occult": "Occult",
        "Philosophy": "Philosophy",
        "Occultism": "Occultism",
        "Fluids": "Fluids",
        "life-spark": "life-spark",
        "spirits": "spirits",
        "Urine": "Urine",
        "Relics": "Relics",
        "echoes": "echoes",
        "memory-trace": "memory-trace",
        "procreation": "procreation",
        "Feasts": "Feasts",
        "Gazetteer": "Gazetteer",
    }
    
    # Apply replacements
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Write the file
    with open('World_of_Eda.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {len(replacements)} typos in World_of_Eda.md")

if __name__ == "__main__":
    fix_typos()
