# RPG Balance Test Plan

## Objective
Validate that the current ruleset achieves the design goal of "fast and dangerous" combat (aiming for 4-5 rounds) and identify statistical imbalances in the "Alpha Strike" initiative system and Resource Economy (Magic/Defense).

## Identified Gaps & Inconsistencies
1. **Damage Calculation**: The text example (34 roll -> +4 dmg) contradicts the rule (Tens digit -> +3 dmg). *Simulation will use the Rule (Tens digit).*
2. **Action Economy**: "Group Turn" initiative may lead to first-turn wipes.
3. **Defense Scarcity**: Defense Actions (MND/10 / 2) might be too scarce for 4-5 round combats.
4. **Magic Viability**: MP costs (5MP/spell vs ~15MP pool) limit casters to ~3 turns of action.

## Simulation Strategy
We will create a script (TypeScript/Python) to simulate thousands of combat iterations.

### 1. Core Mechanics to Model
*   **Dice**: d100 (01-100).
*   **Success**: Roll <= Skill.
*   **Degree of Success (DoS)**: Tens digit of the roll (e.g., 48 -> 4). Criticals (11, 22...) need special handling? *For now, treat as auto-hit + effect.*
*   **Damage**: Weapon Base + DoS - Armor (Temp HP).
*   **Defense**: Pool = Floor(MND / 20)? Text says "Degree of MND / 2". If MND=50, Degree=5, 5/2 = 2. *Simulation will use Floor(MND_Tens / 2).*

### 2. Scenarios
*   **Scenario A: The Duel (1v1)**
    *   Fighter (STR/AGI build) vs Fighter.
    *   Tests: Damage scaling, Defense exhaustion.
*   **Scenario B: The Glass Cannon (1v1)**
    *   Mage (High MND/INT) vs Fighter.
    *   Tests: Can the Mage win before running out of MP?
*   **Scenario C: The Skirmish (Variable Groups)**
    *   **Configuration**: 2-4 Player Characters vs 1-6 Enemy Characters.
    *   **Enemy Variants**: 
        *   Weak (Low Stats, Swarm tactics).
        *   Balanced (Matched stats).
        *   Strong (Boss-like stats, high HP/Dmg).
    *   **Tests**: Impact of numerical advantage vs individual strength ("Action Economy" scaling).

### 3. Metrics to Log
*   **Average Rounds**: Target 4-5.
*   **Win %**: Is it 50/50 for balanced stats?
*   **One-Shot Frequency**: How often does a combat end in Round 1?
*   **Resource Exhaustion**:
    *   % of fights where Mage OOMs (Out of Mana).
    *   % of rounds where Fighter has 0 Defense Actions left.

## Proposed Improvements (To be tested)
*   **Alternative Initiative**: Individual initiative vs Group.
*   **Defense Recharge**: Recover 1 Defense Action per round?
*   **Magic Tuning**: Reduce spell costs or increase MP pool (e.g., MND/2 instead of MND/4).
