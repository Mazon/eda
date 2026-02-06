# Plan: Wait Action Rebalance & Simulation Update

## 1. Problem Statement
The **Wait** action is currently perceived as too powerful because:
- In the **Simulation**, it acts as a free upgrade (Advantage) because the simulation only models one attack per turn regardless of AP cost.
- In the **Rules**, "Momentum" bonuses (+10 Focus) combined with "Rearguard" talents (Vengeful Retort, Exploit Opening) make acting last more attractive than acting first, which devalues winning initiative.
- There is a **Naming Conflict** between the "Focus" talent and the "Focus" momentum benefit.

## 2. Proposed Rule Changes (Core Rulebook.md)

### A. Resolve Naming Conflict
- Rename **Momentum: Focus** to **Momentum: Precision**.

### B. Adjust Wait Mechanic
- **Cost**: 1 Action Point.
- **Momentum (Precision)**: Changed from +10 to **+5 to their next skill check or attack**. (Making it less of a mathematical "must-have" compared to a second attack).
- **Momentum (Brace)**: Remains +2 DR.
- **New Momentum (Observation)**: Gain Advantage on your next **Active Defense** roll (Dodge/Parry/Block) until the start of your next turn. This reinforces the "observe and react" fantasy.

### C. Situationality
- Emphasize that Waiting is best used when:
    - You are out of range and want enemies to move closer.
    - You want to trigger Rearguard talents like **Vengeful Retort**.
    - You need the defensive bonus of **Brace** or **Observation**.

## 3. Simulation Updates (combat_sim.py)

### A. Action Point System
- Update the combat loop to allow 2 AP per character.
- A standard attack costs 1 AP.
- "Wait" costs 1 AP.
- A characther always start their turn with 2 AP to use.

### B. Logic Fix
- Correct the `resolve_attack` loop to ensure "Wait" actually replaces an attack.

## 4. Expected Outcome
Winning initiative (Vanguard) will be the preferred default for maximum damage (2 attacks). Waiting will become a tactical choice for defense or for specific builds that rely on rearguard triggers, rather than a mandatory optimization.
