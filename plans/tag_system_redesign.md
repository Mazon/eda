# Tag-Based Heritage and Talent System Plan

## Objective
Redesign the Heritage and Talent systems into a unified, flexible structure using **Identity Tags**. This removes the rigid "Archetype" silos while maintaining thematic progression.

## 1. The Heritage System (Upbringing)
Heritages represent a character's background. Each Heritage provides an Identity Tag, Skills, and starting equipment.

| Heritage | Identity Tag | Heritage Skills |
| :--- | :--- | :--- |
| **Clansman** | [Clansman] | Survival, Intimidate |
| **Commoner** | [Commoner] | Nature, Athletics |
| **Zealot** | [Zealot] | Religion, Medicine |
| **Noble** | [Noble] | Diplomacy, History |
| **Outcast** | [Outcast] | Streetwise, Intimidate |
| **Artisan** | [Artisan] | Crafting, Engineering |
| **Merchant** | [Merchant] | Barter, Appraise |
| **Veteran** | [Veteran] | Warfare, Athletics |
| **Warden** | [Warden] | Survival, Perception |
| **Wanderer** | [Wanderer] | Occult Knowledge, Investigation |

## 2. The Talent System (Calling)
All talents are moved into a **Master Talent Table**.

### Progression Rules
- **Tier 1**: Open to any character at creation (or later with XP).
- **Tier 2+**: To take a talent of Tier 2 or higher, you must already possess at least one talent with the same Tag in the tier directly below it.

### Tagging Logic
Talents are tagged with the Heritage names they are associated with. Some talents (like magic or music) may have multiple tags, allowing different heritages to access them.

| Name | Tier | Tags | Description |
| :--- | :--- | :--- | :--- |
| **Dirty Fighting** | T1 | [Outcast] | Advantage vs surprised enemies. |
| **Rites** | T1 | [Zealot] | Remove minor curses. |
| **Eldritch Sight** | T1 | [Wanderer], [Zealot] | See magic auras. |
| **Sanctuary of Status**| T1 | [Noble] | Enemies must pass INS check to attack first. |
| **Healing Leaf** | T2 | [Warden], [Commoner]| Create poultice (10 HP). |
| **Hex Craft Novice** | T2 | [Wanderer], [Outcast]| Weave curses/blessings. |
| **Blade Dancer** | T2 | [Noble], [Merchant]| +2 Dmg and advantage on melee for 1 turn. |

## 3. Character Creation Workflow
1.  **Lineage**: Choose attributes.
2.  **Body & Mind**: Calculate HP, IP, and Reactions.
3.  **Heritage**: Select one Heritage.
    - Gain Identity Tag, 2 Skills, Gear, and Currency.
    - **Starting Talent**: Choose **one** Tier 1 Talent from the Master Table that matches your Heritage's Tag.
4.  **Skills**: Select 3 *additional* Trained Skills.
5.  **Combat Styles**: Select 1 Combat Style.
6.  **Course of Life**: Finalize background/goals.

## 4. Implementation Steps
1.  **Core Rulebook.md**:
    - Update 'Character Creation' section.
    - Rewrite 'Heritage' section with the 10 backgrounds and tags.
    - Merge all Archetype Talent trees into a single 'Master Talent Table'.
    - Apply Tags (Heritage names) to all existing talents.
    - Add new talents for [Artisan], [Merchant], [Clansman], and [Commoner] tags.
    - Rename 'Earl' talents to [Noble] tag and 'Thug' talents to [Outcast] tag.
