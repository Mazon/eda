# Cover System Design: Eda Tactical Combat

Cover in Eda is not just a passive bonus; it is a vital part of survival in a world where a single arrow can be lethal. This system is designed to encourage movement, tactical positioning, and meaningful choices between offense and defense.

## 1. Core Mechanics

Cover primarily affects **Ranged Attacks** and certain **Finesse (Thrown)** attacks. It represents the difficulty of hitting a target that is partially or fully obscured by the environment.

### Cover Types
| Type      | Examples                                        | Mechanical Effect                         | Stealth Bonus                            |
| :-------- | :---------------------------------------------- | :---------------------------------------- | :--------------------------------------- |
| **None**  | Open field, empty hallway.                      | No bonus.                                 | Cannot Hide.                             |
| **Light** | Bushes, crates, furniture, other creatures.     | **-10 to Hit** for the attacker.          | Can attempt to **Hide**.                 |
| **Heavy** | Stone walls, large trees, corners, battlements. | **-20 to Hit** for the attacker.          | **Advantage** on Stealth checks to Hide. |
| **Full**  | Behind a solid wall, inside a room.             | **Cannot be targeted** by direct attacks. | Automatic Success (if no LoS).           |

*Note: Area of Effect (AoE) attacks (e.g., Rain Storm, Explosives) ignore Light and Heavy cover unless the defender is behind Full Cover that is airtight/solid enough to block the effect.*

---

## 2. Geometry & Flanking

The effectiveness of cover depends entirely on positioning.

*   **Directional Benefit:** Cover only applies if the object is physically between the attacker and the target. 
*   **Bypassing (Flanking):** If an attacker moves to an angle where the cover no longer obscures the target (typically >45 degrees from the original line), the cover bonus is reduced or removed.
*   **The "Pop-Out" Rule:** When a character in cover attacks, they are assumed to "pop out" briefly. They retain their cover bonus against reactions, but if they use the **Wait** mechanic to act in the Rearguard, they lose their cover bonus until the end of their turn (as they are exposed while aiming).

---

## 3. New Tactical Actions

These actions allow players to interact with the cover system dynamically.

### Hunker Down (Action - 1 AP)
*   **Requirement:** Must be in Light or Heavy cover.
*   **Effect:** You press yourself against the cover. The Cover penalty to attackers increases by an additional **-10** (Light -20, Heavy -30).
*   **Duration:** Lasts until the start of your next turn, you move, or you make an attack.
*   **Penalty:** You cannot make Opportunity Attacks while Hunkered.

### Suppressing Fire (Action - 2 AP)
*   **Requirement:** Ranged weapon equipped.
*   **Effect:** You spray an area with projectiles to keep enemies pinned. Choose a 2m zone or a specific target in cover. Make a **Combat: Ranged** check.
*   **Success:** The target is **Suppressed**. On their next turn, they must spend **1 extra AP** to move out of cover or to make an attack.
*   **Critical Success:** The target is also **Shaken** (-10 to all checks until next turn).

### Leap for Cover (Reaction - 1 Reaction)
*   **Trigger:** When targeted by a Ranged attack.
*   **Effect:** You may immediately move up to **2 meters**. If this movement puts you behind cover (relative to the attacker), you gain that cover's bonus against the triggering attack.

---

## 4. Stealth & Ambush

Cover is the primary prerequisite for the **Stealth** skill in combat.

*   **Vanishing:** A character in Light or Heavy cover can spend 1 AP to make a **Stealth vs Perception** check to become **Hidden**.
*   **Hidden Status:** Enemies cannot target a Hidden character unless they spend an Action to **Search** or move to a position where the character is no longer obscured.
*   **Ambush:** Attacking from Hidden grants **Advantage** on the attack roll and deals **+DoS** additional damage.

---

## 5. Talent Integration

*   **Calm Shooting (T1):** Now a Passive. Your ranged attacks treat Heavy Cover as Light Cover, and ignore Light Cover.
*   **Smart Fighting (T1):** While in cover, you gain **+10** to all Active Defense rolls (Dodge, Parry, Block).
*   **Shadow Step (T2):** You can move between two points of Heavy Cover within 10m without being seen or triggering Opportunity Attacks.

---

## 6. Implementation Notes for GM
*   **Destructible Cover:** Wooden crates (HP 5, DR 1) or thin fences can be destroyed by heavy attacks, removing the cover bonus.
*   **Crowded Combat:** In tight corridors, allies can provide Light Cover for each other, but this also means a "Miss" against the intended target might hit the ally providing cover (GM's discretion on a roll of 90-100).
