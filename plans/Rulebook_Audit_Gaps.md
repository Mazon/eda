# Comprehensive Rulebook Audit: Gaps & Ambiguities

This document identifies poorly defined rules, missing mechanics, and logical inconsistencies within the current Eda Core Rulebook.

## 1. Core Mechanics & Math Issues

### Degree of Success (DoS)
*   **Ambiguity**: [RESOLVED] DoS is defined as the tens digit of the roll.
*   **Inconsistency**: [RESOLVED] Difficulty levels have been rebalanced (Routine 1, Challenge 2, Hard 4, Extreme 6, Near Impossible 8) to scale better with high skill levels. Critical Successes now bypass DoS requirements to ensure low-skill characters always have a slim chance.

### Reactions Pool
*   **The "Encounter" Problem**: Reactions are a pool for the *entire encounter* (e.g., 2-3 reactions total). 
*   **Ambiguity**: Does "encounter" mean one fight? If a fight lasts 5 rounds, and you are attacked twice per round, you run out of reactions by Round 2. This makes Active Defense almost non-existent for 80% of a fight.
*   **Talent Interaction**: Many talents (Blocker, Dodge, Parry) "unlock" or use reactions. If the pool is empty, these talents become useless.

### Movement & AP
*   **Undefined Range**: Many spells and talents (e.g., "Nearby", "Aura") don't have specific meter ranges.
*   **Diagonal Movement**: No rule for diagonal movement on a grid (if used).

---

## 2. Character Creation & Heritage Gaps

### Nature Imbalance
*   The stat arrays are inconsistently totaled (some 360, some 380, some 340 in previous drafts - current rulebook shows all at 360 but "The Lynx" and "The Raven" often drift in character sheets). *Verify against character sheet template.*

### Heritage Trait Vagueness
*   **Hearth-born (Stoic Endurance)**: "Ignore all penalties from Exhaustion or Cold". What are the penalties for Exhaustion or Cold? They are not defined in the rulebook.
*   **Dvergr (Starting Equipment)**: "A pouch of Deep-Salt". No mechanical effect listed.
*   **Warg-touched (Primal Instinct)**: "See in low light as if it were bright light". How does "dim light" or "darkness" mechanically affect characters who *don't* have this? (e.g., Disadvantage? -20 to hit?).

---

## 3. Skills & Talents (The "Dead End" Rules)

### Missing Skill Descriptions
*   **Acrobatics/Athletics**: No specific DCs or examples (how high can I jump? how far can I fall?).
*   **Engineering**: Mentioned as a Heritage skill for Dvergr, but what can you actually *do* with it? No crafting/repair rules.
*   **Investigation**: Linked to CHA in the table. Usually, this is INT. This makes "The Raven" worse at investigating than the "The Fox".

### Poorly Defined Talents
*   **Endurance Training (T1)**: "Increase Max HP (amount undefined)". This is unusable as written.
*   **Animal Handler (T1)**: "Pet mechanics". No mechanics provided.
*   **False Persona (T1)**: "Cannot use other talents". Why? Does this include passive talents?
*   **Far Throwing (T2)**: "Throw humanoid 20m". Does this require a check? Is there damage? 20m is a massive distance (4-5 stories high).
*   **Tactical Guard (T2)**: "+10 to their next Defense roll". There are no "Defense rolls", only AGI checks (Dodge) or Skill checks (Parry/Block).
*   **Jack of all Trades (T2)**: "Lowest skills set to second-lowest value". This is extremely complex to track as skills improve.
*   **Hex Craft Novice (T2)**: "Weave curses/blessings". None are listed for this specific talent level.
*   **Spirit Walker (T3)**: "Commune with spirits". No rules for what spirits know or how they interact.
*   **Heirloom Relic (T3)**: "Item with +5 bonus". +5 to what? Damage? Hit? A skill?

---

## 4. Combat & Equipment Gaps

### Damage & Weapons
*   **Weapon Traits**: "Fast", "Versatile", "Loading", "AP". None of these are defined in the Equipment section.
*   **Critical Success**: "Max Damage: Weapon Base Damage + tens digit of the Skill".
    *   Example: Great Sword (10) + Skill 70 (+7) = 17 Damage.
    *   Normal Hit: 10 + DoS. If you roll a 15 (Success), you deal 10 + 1 = 11.
    *   Issue: A Critical Success is barely better than a high-rolling normal hit, but much rarer.

### Armor & Health
*   **Armor Requirements**: "STR > 70". The highest starting STR is 70 (The Bear). This means most characters can never wear Plate Armor without spending 10 XP to increase STR.
*   **Armor DR vs Shield DR**: The rules for "Block" say "Double Shield DR + STR Bonus", but the Shield table says "Shields are used with the Block reaction... add the shield's DR to your armor's DR". These are two different calculations.

---

## 5. Magic & Rituals

### Spell Ambiguity
*   **MP Limit**: MND / 4. With a MND of 60, you have 15 MP. Spells cost 5-10 MP. You can cast 2-3 spells per *adventure*? Or per *day*? The refresh rate for MP is never stated.
*   **Success Checks**: Do spells require a roll? (e.g., MND check?). "Freeze in Place: Chance to immobilize". What is the chance? What is the save?
*   **Duration**: Most spells (Confuse, Rain Storm, Form of a Beast) have no duration listed.

### Rituals
*   **Material Costs**: Listed in "g" (Gold?), but the economy uses "sp" (Silver Pieces). Is 1g = 10sp? This conversion is missing.
*   **Summon Python**: "Summons a Giant Snake (Bestiary)". There is no Giant Snake in the current document (it's in a separate file, but stats should be accessible or summarized).

---

## 6. Progression & GMing

### XP Spending
*   **Steady Training**: "Spend XP to increase a skill by that many points". This is incredibly cheap compared to Attributes (10 XP for +1). You could spend 5 XP to get +5 to a skill, or 10 XP to get +1 to the Attribute (which gives +1 to *all* associated skills). 
*   **Missing "Levels"**: The rulebook doesn't define what a "Level 1" vs "Level 5" character looks like, despite being used in the campaign books.

### Madness & Sanity
*   **Mind Point Death**: Characters now die at 0 Mind Points. Need to define if there are any "threshold" effects before death (e.g., temporary insanity).
