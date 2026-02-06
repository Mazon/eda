# Defense & Combat Redesign Proposal

Based on your feedback, we are moving away from **Ablative Armor** (tracking armor HP) to a streamlined system that emphasizes **Active Defense** and tactical choices, while keeping Armor simple and balanced.

## Core Philosophy
1.  **No Tracking:** Armor does not have "HP". You don't need to erase/update values during combat.
2.  **Active Survival:** Standing still and taking hits is deadly. You must use **Reactions** (Dodge, Parry, Block) to survive.
3.  **Armor as Mitigation:** Armor reduces the severity of mistakes (Damage Reduction), but it won't save you from a direct hit by a giant.
4.  **Symmetry:** Enemies obey the same rules. They don't have massive armor pools.

---

## 1. Armor: Passive Damage Reduction (DR)
Armor provides a small, constant reduction to incoming damage. It represents the armor turning a lethal blow into a bruise or glancing hit.

| Armor Type     | DR (Damage Reduction) | Notes                         |
| :------------- | :-------------------: | :---------------------------- |
| **Clothes**    |           0           | -                             |
| **Leather**    |           1           | Light.                        |
| **Chain Mail** |           2           | Moderate protection.          |
| **Plate**      |           3           | Good protection.              |
| **Shield**     |          +1           | Passive coverage (stackable). |

*   **Impact:** A dagger dealing 5 damage becomes 2 damage against Plate. A Giant dealing 15 damage becomes 12. Armor helps against small hits but requires Active Defense for big ones.

## 2. Active Defense (Reactions)
Every character has **1 Reaction per round** (or more with Talents like *Defender*). Using a Reaction correctly is key to survival.

### A. Dodge (AGI)
*   **Mechanic:** Roll **AGI**.
*   **Success:** Avoid **ALL** damage.
*   **Failure:** Take full damage.
*   **Best For:** High AGI characters, avoiding massive single hits (like a Giant's club).
*   **Risk:** All-or-nothing.

### B. Parry (Combat Skill)
*   **Mechanic:** Roll **Combat Skill** (Melee).
*   **Success:** Reduce damage by **Weapon Damage + STR/AGI Bonus**.
*   **Failure:** Take full damage.
*   **Best For:** Duelists, fighting armed opponents.
*   **Note:** Cannot parry massive attacks (Giants, Dragon Breath) or ranged attacks (unless specific Talent).

### C. Block (Shield Skill)
*   **Mechanic:** Roll **Shield Skill**.
*   **Success:** Reduce damage by **Shield Block Value** (e.g., 8-12) + **STR Bonus**.
*   **Failure:** Take half damage (Shield still absorbs some impact).
*   **Best For:** Tanks, reliable mitigation against everything.

## 3. Enemy Balance
Enemies will no longer have "Armor HP". Instead:
*   **Standard Enemies:** 0-1 DR (Thick skin, rusty armor).
*   **Elite/Bosses:** 2-3 DR (Plate, Scales).
*   **HP:** adjusted to compensate.

## 4. Example Combat Flow
**Scenario:** An Orc swings an axe at generic Hero (Leather Armor, DR 1).
1.  **Orc Attack:** Hits! Damage is 8.
2.  **Hero Reaction:**
    *   *Option A (Take it):* Takes 8 - 1 (DR) = **7 Damage**.
    *   *Option B (Dodge):* Rolls AGI... Success! **0 Damage**.
    *   *Option C (Parry):* Rolls Sword Skill... Success! Deflects 6 damage. Takes 8 - 6 - 1 (DR) = **1 Damage**.

## 5. Comparison
| Feature      | Old System (Ablative)         | New Proposal (Active)                |
| :----------- | :---------------------------- | :----------------------------------- |
| **Tracking** | Armor HP (erasing constantly) | None (Static values)                 |
| **Defense**  | Passive buffer                | Active choice (Dodge/Parry/Block)    |
| **Feel**     | "I have 20 extra HP"          | "I narrowly dodged that swing!"      |
| **Balance**  | Armor was mandatory           | Armor is helpful, Skill is mandatory |

---

## Decisions Needed
1.  **Do you like the Low DR (1-3) range?** Or should it be slightly higher (2-5)?
2.  **Do you agree with the "Reaction" system?** (Dodge/Parry/Block)?
