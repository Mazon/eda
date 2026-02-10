# Wound & Critical Injury System

## Core Mechanics

### 1. Bleeding
Every attack that deals damage (after armor reduction) inflicts a **Bleed**.
*   **Trigger:** Any damaging hit.
*   **Effect:** Bleeding acts as **Negative Damage Reduction**. For every stack of Bleeding you have, you take **+1 extra damage** from all future attacks.
    *   *Example:* If you have 3 Bleeding stacks and an enemy hits you for 5 damage, you take **8 damage** (5 + 3).
*   **Stacking:** Bleeding stacks indefinitely during combat.
*   **Duration:** Bleeding stacks persist until the end of the combat encounter, representing the cumulative toll of minor injuries opening up your defenses.
*   **Treatment:** A successful **Medicine check** (Action) can remove all bleed. 

### 2. Injuries
When a character suffers a **Critical Hit** (rolling doubles under the attacker's skill, e.g., 11, 22, 33), they suffer a **Injury** in addition to the normal damage.
*   **Roll:** The combatant that did the critical hit rolls a d100 on the **Injury Table**.
*   **Effect:** The table provides both a narrative description and a mechanical penalty (e.g., Stunned, Disadvantage, Broken Limb).
*   **Note:** Injuries are distinct from Bleeding and have their own specific durations/cures.

## Injury Table (d100)

| Roll      | Severity     | Narrative Prompt                                            | Mechanical Effect                                                                                      |
| :-------- | :----------- | :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| **01-10** | **Minor**    | **Glancing Blow** - A jarring hit that rattles you.         | **Stunned:** You lose your next Half Action.                                                           |
| **11-20** | **Minor**    | **Deep Gash** - A painful cut but clean.                    | **Pain:** -10 to your next check due to shock.                                                         |
| **21-30** | **Minor**    | **Knocked Senseless** - Ringing ears and blurred vision.    | **Disoriented:** Disadvantage on all Logic and Instinct checks for 1d4 rounds.                         |
| **31-40** | **Moderate** | **Leg Wound** - Muscle torn or bone chipped in the leg.     | **Hobbled:** Movement speed halved until healed.                                                       |
| **41-50** | **Moderate** | **Arm Wound** - Deep trauma to the arm or shoulder.         | **Weakened Grip:** Disadvantage on checks using that arm (Attacks, Climbing) until healed.             |
| **51-60** | **Moderate** | **Head Trauma** - A severe blow to the skull.               | **Concussion:** -10 to Logic and Instinct permanently (or until fully rested/healed).                  |
| **61-70** | **Severe**   | **Broken Ribs** - Breathing is agony.                       | **Winded:** You cannot take the "Sprint" action. -10 to Constitution checks.                           |
| **71-80** | **Severe**   | **Internal Injury** - Organs bruised or ruptured.           | **Vulnerable:** You take double damage from Bleeding stacks (e.g., +2 damage per stack instead of +1). |
| **81-85** | **Severe**   | **Mangled Limb** - An arm or leg is crushed or ruined.      | **Useless Limb:** The limb is unusable. If leg, prone and crawl only. If arm, drop items.              |
| **86-90** | **Severe**   | **Severed Extremity** - Fingers, toes, ear, or nose lost.   | **Permanent Loss:** -5 to relevant checks (e.g., Dexterity, Charisma) permanently.                     |
| **91-95** | **Lethal**   | **Mortal Wound** - A strike to the heart, throat, or brain. | **Dying:** You immediately drop to 0 HP and begin dying.                                               |
| **96-99** | **Lethal**   | **Severed Limb** - Arm or leg chopped off.                  | **Amputation:** Limb is gone. Constitution check or pass out immediately.                              |
| **00**    | **Fatality** | **Instant Death** - Decapitation or heart destroyed.        | **Dead:** Character is instantly killed.                                                               |

## Healing & Recovery
*   **Bleeding:** Removed automatically at end of combat, or via Medicine (Action) during combat.
*   **Minor Injuries:** Heal naturally after a Long Rest.
*   **Moderate Injuries:** Require Medical attention.
*   **Severe Injuries:** Require Surgery.
*   **Lethal/Permanent:** Require high-level Magic or unique prosthetics to mitigate.
