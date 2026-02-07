# Mechanics Audit and Proposal for Eda

## 1. Mechanics Audit: Consistency & "Mid-Roll" Flat Bonuses

The core philosophy of Eda is "roll once" using 2d10. Flat bonuses added *during* a roll (e.g., `+10 to Hit` from a talent) slow down play compared to Advantage/Disadvantage. Static bonuses (e.g., `+5 Damage` on character sheet) are fine as they are calculated once.

### 1.1 Poorly Defined or Inconsistent Mechanics

| Mechanic                      | Issue                                                                                                                                   | Recommendation                                                                                                                                              |
| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Reaction Pool Calculation** | Text says `(AGI / 2) / 10` but example says `MND / 2`.                                                                                  | **New Standard**: Reaction Pool = **Tens digit of AGI** (e.g., AGI 65 = 6 Reactions). This is easier to calculate and incentivizes high agility.            |
| **Spells (Non-Ritual)**       | "MND check" lacks Difficulty (DoS) or TN.                                                                                               | Assign DoS requirements (e.g., *Confuse*: Routine 1 DoS).                                                                                                   |
| **Dodge Difficulty**          | Dodge currently provides **Full Protection** on success. Because it is binary (all or nothing), it needs to be harder than Block/Parry. | Change Dodge to a **Challenge (2 DoS)** requirement by default. This makes it a high-risk/high-reward gamble compared to the reliable reduction of a Block. |

### 1.2 "Mid-Roll" Flat Bonus Audit (Targets for Removal)

These mechanics currently require mental math during the roll and should be converted to **Advantage** or **Static Effects**.

| Current Mechanic                | Current Effect                    | Proposed "Smooth" Change                                                        |
| :------------------------------ | :-------------------------------- | :------------------------------------------------------------------------------ |
| **Precision (Momentum)**        | +10 to next check.                | Change to **Advantage** on next check.                                          |
| **Talent: Berserk**             | +20 Attack, No Defense.           | Change to **Advantage** on all attacks, cannot use Reactions.                   |
| **Talent: Smart Fighting**      | +10 to Active Defense in cover.   | Change to **Advantage** on Active Defense in cover.                             |
| **Talent: Holy Aura**           | +10 to Active Defense for allies. | Change to **Advantage** on Active Defense for allies.                           |
| **Talent: Coordinated Assault** | +10 to Hit if ally hit target.    | Change to **Advantage** on the attack.                                          |
| **Talent: Commanding Presence** | Allies +5 Attack/Skill.           | Change to **Advantage** on the next check (1/turn) or a static bonus to damage. |
| **Talent: Evasive Maneuver**    | +10 to Active Defense if moved.   | Change to **Advantage** on Active Defense until next turn.                      |
| **Talent: Inspiring Presence**  | Allies +20% Attack/Saves.         | Change to **Advantage** on the first roll of the encounter.                     |

---

## 2. Implementation Roadmap

1.  **Remove Mid-Roll Math**: Systematically replace all `+10 to Hit/Defense` talents with **Advantage**. 
2.  **Stat-Sheet Bonuses**: Keep `+Damage` or `+Armor DR` as they are calculated once and noted down.
3.  **Spell Difficulty**: Update the Spell Table to include DoS requirements.
4.  **Reaction Pool Fix**: Update character creation to use **Tens digit of AGI** for Reaction Pool.
5.  **Dodge Rebalance**: Update Dodge to require **2 Degrees of Success** to reflect its power as a full-negation mechanic.
