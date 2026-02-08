# Eda Publication Readiness Plan

This plan outlines the steps required to refine the Eda rulebooks for professional publication.

## 1. Core Terminology Standardization
We will adopt a strict set of abbreviations and terms to ensure the rules are easy to read and internally consistent.

| Term                  | Abbreviation | Usage Rule                                                                |
| :-------------------- | :----------- | :------------------------------------------------------------------------ |
| **Degree of Success** | DoS          | Always use "Degree of Success" on first mention in a section, then "DoS". |
| **Action Point**      | AP           | Use for mechanical costs (e.g., 1 AP).                                    |
| **Silver Piece**      | sp           | Use for all currency mentions. (100 cp = 1 sp, 100 sp = 1 gp).            |
| **Instinct Points**   | IP           | Mental/Magic pool.                                                        |
| **Health Points**     | HP           | Physical pool.                                                            |
| **Defense**           | -            | Use "Defense" instead of "DR" or "Armor Reduction".                       |
| **Game Master**       | GM           | Standard RPG term.                                                        |
| **Player Character**  | PC           | Standard RPG term.                                                        |

## 2. Structural & Layout Improvements
*   **Header Consistency**: Ensure a logical flow:
    *   `#` (H1) for Main Books/Chapters.
    *   `##` (H2) for Major Sections (Dice Mechanics, Character Creation, Combat).
    *   `###` (H3) for Sub-sections (Initiative, Actions, Damage).
    *   `####` (H4) for specific list items or small details.
*   **Consolidation**: Move all "Blackjack System" and "Degree of Success" explanations into a single "Core Mechanics" section to avoid repetition.
*   **Table Formatting**: Standardize all tables with the CSS-defined headers.
*   **Callout Boxes**: Standardize example boxes with `> ### Example: [Title]`.

## 3. Rule Clarification & Mechanical Refinement
*   **Blackjack System**: Clearly state: "Roll as high as possible without exceeding your skill. The tens digit is your Degree of Success (DoS)."
*   **Reaction Pool**: Explicitly state that reactions do not refresh per round, but per encounter, unless specific talents (like *Vanguard Reflexes*) are used.
*   **Evasive Maneuver**: Clarify if the advantage on Active Defense lasts for the *entire* round after moving 3m, or only until the next action.
*   **Dodge Difficulty**: Ensure the 2 DoS requirement for Dodge is clearly labeled in the core rules, not just the talent description.

## 4. Cross-Book Alignment
*   **Bestiary.md**: Update all monster entries to use "Defense" and ensure "Reactions" are clearly defined as a finite pool.
*   **Character Sheet.md**: Verify that the sheet fields (e.g., "Reaction Pool") match the finalized terminology.

## 5. Final Polish
*   **PDF Generation Test**: Run the `scripts/generate_pdfs.py` to ensure the Markdown changes render correctly with the `scripts/style.css`.
*   **Proofreading**: One final pass for typos (e.g., "iniative", "resis").
