# Proposal: Difficulty Modifier & Degree of Success Rebalance

## Problem Statement
The current Difficulty Modifiers use a flat "Degree of Success" (DoS) requirement that scales poorly with higher skill values. 
A "Near Impossible" task currently requires only 3 DoS (rolling 30+ while remaining under the skill).
For a character with 75% skill, this results in a **46% chance of success**, which contradicts the "Near Impossible" label.

## Current Scaling (Skill 75%)
| Difficulty      | DoS Req | Roll Range | Chance |
| :-------------- | :------ | :--------- | :----- |
| Challenge       | 1       | 10-75      | 66%    |
| Hard            | 2       | 20-75      | 56%    |
| Near Impossible | 3       | 30-75      | 46%    |

## Proposed Scaling
We should increase the DoS requirements for higher difficulties and add a "Crit Bypass" to allow low-skill characters a slim chance at high-difficulty tasks.

### Revised Difficulty Table
| Difficulty          | Requirement | 75% Skill Chance | 30% Skill Chance | Description                      |
| :------------------ | :---------- | :--------------- | :--------------- | :------------------------------- |
| **Easy**            | 0 DoS       | 75%              | 30%              | Simple tasks with no pressure.   |
| **Routine**         | 1 DoS       | 66%              | 21%              | Standard professional tasks.     |
| **Challenge**       | 2 DoS       | 56%              | 11%              | Demanding tasks requiring focus. |
| **Hard**            | 4 DoS       | 36%              | Impossible*      | Significant obstacles.           |
| **Extreme**         | 6 DoS       | 16%              | Impossible*      | At the edge of human capability. |
| **Near Impossible** | 8 DoS       | Impossible*      | Impossible*      | Practically legendary feats.     |

*\*Note: Critical Successes (Doubles) bypass DoS requirements.*

### The "Crit Bypass" Rule
To ensure that even "Impossible" tasks have a tiny chance of success (and to reward high skill), we propose:
> **Critical Success & Difficulty**: A Critical Success (rolling doubles under your skill) automatically provides the required Degrees of Success for the check, regardless of the difficulty.

**New Chances with Crit Bypass:**
- **30% Skill**: Has a 2% chance (rolls 11, 22) to succeed at *any* difficulty.
- **75% Skill**: Has a 6% chance (rolls 11, 22, 33, 44, 55, 66) to succeed at "Near Impossible" (8 DoS), even though their skill is normally too low to hit the required DoS.

## Impact on Combat
DoS is currently used for damage calculation. This change primarily affects **Non-Combat Checks** and **Active Defense** (if difficulty modifiers are applied there). 

## Implementation Plan
1. Update `Core Rulebook.md` with the new Difficulty Table.
2. Add the "Crit Bypass" rule to the Checks section.
3. Update `combat_sim.py` if it uses difficulty thresholds for any logic.
