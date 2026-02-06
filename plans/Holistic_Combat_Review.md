# Holistic Combat Review & Fun Factor

## 1. The "Fun" of Hitting
You mentioned the **65-85% hit rate sweet spot**.
*   **Current State:** Base Skill = Attribute / 2 (~30%). Max Hit ~60%.
    *   Result: Players miss too often, especially with Heavy Attack (-20% -> 40% hit).
*   **Proposal:** Change Base Skill to **Full Attribute Value**.
    *   Start: ~60%.
    *   With Weapon (+10): ~70%.
    *   With Talents (+10): ~80%.
    *   **Result:** Standard attacks hit reliably (Satisfying). Heavy Attacks (-20%) drop to ~60% (Risky but viable).

## 2. Shields & Equipment
*   **Issue:** The simulation currently assumes a character holding a "Shield" weapon cannot attack effectively, or has no weapon.
*   **Fix:** Add an **Offhand Slot**.
    *   **Shields:** Provide +1 Passive DR and unlock the **Block** reaction (Soak 15 damage).
    *   **Dual Wield:** Unlock **Parry** with higher bonus.

## 3. Dynamic Talents (Making it Interesting)
We are currently using basic passive talents. We need active, exciting ones.
*   **Shield Bash (Active):** Attack with Shield. Low damage but **Stuns** target (lose next turn).
*   **Cleave (Passive):** When you kill an enemy, make a free attack against another nearby. (Makes fighting minions fun).
*   **Precision (Passive):** +10 Hit Chance. (For the "Sniper" archetype).

## 4. Simulation "Fun Metrics"
We will track:
*   **Hit Rate:** Average % of attacks that land.
*   **Turn Efficiency:** How many turns to kill an average enemy? (Target: 2-3 rounds).
*   **Survival Rate:** How often do players reach 0 HP?

---

## Action Plan
1.  **Rule Change:** Update Base Skill calculation in Rulebook/Sim.
2.  **Code:** Add `offhand` to Character. Update `create_party` to equip Shields.
3.  **Code:** Implement `Shield Bash` and `Cleave` in combat logic.
