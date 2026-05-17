# Project Structure: Terraforming Mars Strategy Agent

This project is a specialized knowledge base and strategy engine for the board game *Terraforming Mars*. It is designed to be used by AI agents to provide expert analysis and game-state recommendations.

## Core Components

### 1. Skills Directory (`.agents/skills/`)
The primary source of domain knowledge. Skills are organized by card type and name:
- `tm-corp-*`: Data and strategic analysis for Corporations.
- `tm-prelude-*`: Data and strategic analysis for Prelude cards.
- `tm-project-*`: Data and strategic analysis for Project cards.
- `tm-rules`: The "Source of Truth" for game rules, setup phases, and logic.
- `general-strategy`: Foundational heuristics for resource management and engine building.

### 2. Instruction Hierarchy
- **`agents.md` (This file):** Explains project formation and how to use the available tools.
- **`SKILL.md` (Within each skill):** Contains the actual data, effects, and expert commentary for a specific card or rule set.

## Agent Workflow
When analyzing a game state or providing recommendations:
1. **Initialize Rules:** Always load `tm-rules` first to establish the logic for the current phase.
2. **Activate Skills:** Use `activate_skill` for the specific cards in play to access their internal "Strategic Analysis" and "Tips".
3. **Synergy Check:** Compare activated skills to identify "God-Tier" combos or "Trap" cards.
4. **Context Efficiency:** Use `grep_search` to find cards by tag or effect when the specific card names are unknown.
