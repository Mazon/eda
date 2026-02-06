# Combat Improvement Architecture: Eda Evolution

After analyzing the Core Rulebook, the Age of Wolves campaign, the Bestiary, and running the simulation script, I have identified several key areas where combat can be deepened, balanced, and made more evocative of Eda's dark fantasy tone.

## 1. The "Reaction Economy" Problem
**Observation:** Characters have a limited pool of reactions for an *entire encounter*. While this creates tension, it leads to a "cliff" where players suddenly become defenseless after 2-3 rounds, making longer boss fights (like Fenrir) feel like a death sentence.
**Proposal:** 
*   **Partial Refresh:** Allow characters to recover **1 Reaction** at the start of each round, up to their maximum pool. This keeps the pool relevant throughout long fights while still requiring careful management.
*   **Desperate Reactions:** Allow players to "push" themselves by spending 2 **Mind Points** to gain an immediate reaction, representing a surge of desperate adrenaline. This carries the risk of death if MP reaches 0.

## 2. Initiative & The Wait Mechanic
**Observation:** The Wait mechanic is mechanically solid but underutilized because the "Momentum" benefits are sometimes weaker than just attacking early.
**Proposal:**
*   **Tactical Lead:** If a player Waits and then successfully hits an enemy, they grant **Advantage** to the next ally's attack against that same enemy. This encourages "setting up" big hits.
*   **Intervention:** Allow a player who has "Waited" to interrupt an enemy action (using their held action) if the enemy enters their reach or targets an ally.

## 3. Defense Scaling
**Observation:** Dodge (AGI-based) is currently all-or-nothing, while Parry and Block are safer but require specific skills. Heavier armor makes you easier to hit but reduces damage.
**Proposal:**
*   **Glancing Blows:** If a Dodge fails by less than 10, it counts as a "Glancing Blow." The character takes half damage instead of full.
*   **Shield Durability:** High-damage attacks (e.g., from Giants or Bosses) should have a chance to "break" a block, forcing a STR check to avoid being knocked Prone even on a successful block.

## 4. Bestiary Depth
**Observation:** Monsters are currently "bags of HP" with 1-2 abilities.
**Proposal:**
*   **Staged Bosses:** As seen in the Fenrir sim, bosses need clear "Phases." 
    *   *Phase 1:* High DR, slow attacks.
    *   *Phase 2:* Low DR, multiple fast attacks, area effects.
*   **Environmental Synergies:** Give monsters abilities that interact with the map (e.g., Spiders pulling enemies into webbing "zones," or Draugr creating patches of "Freezing Ground" that reduce AGI).

## 5. Simulation Results Analysis
The simulation showed a **3% Campaign Win Rate**, primarily failing at **Fenrir Phase 1 (18% win rate)** and **Draugr Warriors (67% win rate)**.
*   **Issue:** The "death spiral" in Eda is very fast. Once a character hits <10 HP, they lose avoidance, leading to a quick death.
*   **Fix:** Introduce **"Second Wind"** – once per long rest, when a character hits 0 HP, they can make a CON check to stay at 1 HP and gain 10 Temp HP for 1 round.

## 6. Action Economy Variety
**Observation:** 2 Action Points are usually spent on "Attack + Attack" or "Move + Attack."
**Proposal:**
*   **Utility Actions (1 AP):**
    *   **Shove:** Push an enemy 2m (STR vs STR).
    *   **Feint:** Next attack has +10 Hit (AGI vs MND).
    *   **Protect:** Grant +1 DR to an adjacent ally until next turn.

---
**Next Steps:**
1. Implement the "Partial Refresh" of reactions in the `combat_sim.py`.
2. Update the `Core Rulebook.md` with the "Glancing Blow" and "Tactical Lead" rules.
3. Add "Phase" logic to the Bestiary for legendary creatures.
