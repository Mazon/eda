# Eda

> *Winter had arrived, snowflakes gently falling down to the ground...*

**Eda** is a dark fantasy tabletop roleplaying game of magic, wonder, and perilous adventure. In a world filled with supernatural forces, magic often carries heavy consequences, and life is harsh for those who dare to wield it.

## 📚 Contents

This repository contains the source files for the Eda TTRPG system, including:

- **[Core Rulebook](Core%20Rulebook.md)**: The complete rules for playing and running the game.
- **[Bestiary](Bestiary.md)**: A collection of monsters and creatures to challenge players.
- **Adventures**: Ready-to-play modules like *[The Age of Wolves](Adventure_The_Age_of_Wolves.md)*.
- **Character Sheets**: Tools for creating and managing characters.

## 🛠️ Tools & Scripts

The project includes several utility scripts located in the `scripts/` directory:

- `generate_pdfs.py`: Automates the conversion of Markdown source files into formatted PDFs (requires Pandoc).
- `combat_sim.py`: A Python-based combat simulator to test game balance and mechanics.
- `generate_interactive_sheet.py`: Generates the interactive HTML character sheet.

## 🚀 Getting Started

### Prerequisites

To build the documentation locally, you will need:
- Python 3.10+
- [Pandoc](https://pandoc.org/installing.html) (for PDF generation)

### Generating PDFs

To build the rulebooks and adventure modules into PDFs:

```bash
python ./scripts/generate_pdfs.py
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
