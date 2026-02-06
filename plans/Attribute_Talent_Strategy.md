# Attribute & Talent Optimization Strategy

Instead of adding new equipment tiers, we can explore how optimizing **Attribute growth** and **Talent synergies** within the existing core rules affects combat duration and balance.

## 1. Reaction Pool Management (The MND Strategy)
Currently, reactions are the primary defense.
- **Hypothesis:** If characters prioritize **MND** early, their reaction pool increases. A larger pool allows them to survive more "high damage" hits, naturally extending combat rounds without increasing HP or DR.
- **Rulebook Context:** Reactions = (MND/2) tens digit. Increasing MND from 40 to 60 moves reactions from 2 to 3.

## 2. Attribute Synergies (CON vs AGI)
- **Survival Strategy:** If characters focus on **CON** to its natural cap (Attribute + 40), they gain more HP (HP=CON/2), making them less prone to "sudden death."
- **Accuracy Strategy:** Focusing on **AGI/STR** and **Combat Skill** ensures they don't miss, which prevents the "stalemate" effect where combat lasts too long but feels unrewarding.

## 3. Talent Combo Optimization
We can simulate specific "builds" to see if they solve the Book 4 problem:
- **The Tank:** Blocker (T1) + Guardian (T2) + Durable (T3). Uses Shield and high CON to absorb hits.
- **The Striker:** Focus (T1) + Overdrive (T1) + Weapon Specialization (T2) + Empower (T2). Maximizes damage per action to end boss phases faster.
- **The Support:** Commanding Presence (T1) + Bolster (T2). Improves accuracy for the whole party.

## 4. Proposed Simulator Adjustments
1.  **Smart Leveling:** Update the `spend_ap()` logic to follow these "build" paths rather than random distribution.
2.  **Strategic Reactions:** Characters save reactions for hits that would deal >15% HP or when they are <30% HP.
3.  **Simulation Goal:** Determine if "Optimal Play" (using only core rules) allows for a >70% win rate in Book 4.

Please let me know if you prefer this approach over the Equipment-based scaling!
