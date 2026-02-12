# Eda

> *Winter had arrived, snowflakes gently falling down to the ground...*

**Eda** is a dark fantasy tabletop roleplaying game of magic, wonder, and perilous adventure. In a world filled with supernatural forces, magic often carries heavy consequences, and life is harsh for those who dare to wield it.

## 📚 Contents

This repository contains the source files for the Eda TTRPG system, including:

- **[Core Rulebook](Core%20Rulebook.md)**: The complete rules for playing and running the game.
- **[World of Eda](World_of_Eda.md)**: (GM Only) Detailed world description, factions, and random tables.
- **[Creature Compendium](Creature_Compendium.md)**: A collection of monsters and creatures to challenge players.
- **Adventures**: Ready-to-play modules like *[The Age of Wolves](Adventure_The_Age_of_Wolves.md)*.
- **Character Sheets**: Tools for creating and managing characters.

## 🛠️ Tools & Scripts

The project includes several utility scripts located in the `scripts/` directory:

- `build.py`: Main build script for generating all PDFs from Markdown and HTML sources (requires Pandoc and WeasyPrint).
- `combat_sim.py`: A Python-based combat simulator to test game balance and mechanics.
- `prepare_html.py`: Prepares the interactive character sheet HTML for PDF generation.
- `generate_interactive_sheet.py`: Generates the interactive PDF character sheet.

## 🚀 Getting Started

### Prerequisites

To build the documentation locally, you will need:
- Python 3.10+
- [Pandoc](https://pandoc.org/installing.html) (for Markdown to HTML conversion)
- WeasyPrint (for HTML to PDF conversion): `pip install weasyprint`

For detailed build instructions, see [BUILD.md](BUILD.md).

### Generating PDFs

To build all rulebooks and adventure modules into PDFs:

```bash
python ./scripts/build.py
```

To build a specific file:

```bash
python ./scripts/build.py "Core Rulebook.md"
```

To check if all dependencies are installed:

```bash
python ./scripts/build.py --check
```

The generated files will be output to the `build/` directory.

### Running Combat Simulations

To run the combat simulator:

```bash
python ./scripts/combat_sim.py
```

## 📄 License

This project is currently under development.

---

*“The name Eda itself is said to mean 'Wondrous' in a long-forgotten tongue.”*
