# Project Instructions: Terraforming Mars Agent Training

## Skill Development
- **Skill Location:** All new skills MUST be created within the `.agents/skills/` directory.
- **Conflict Prevention:** Never use the `.gemini/skills/` directory for project-specific skills to avoid path conflicts.
- **Standard Structure:** Follow the alphabetical naming convention `tm-<type>-<name>` (e.g., `tm-project-trees`, `tm-corp-credicor`).

## Strategic Analysis Mandate
- **No Premature Analysis:** NEVER provide strategic tips, evaluations, or "hints" until you have first activated the individual skills for EVERY card involved in the context (e.g., all Corporations, Preludes, and Project cards in a hand).
- **Mandatory Sequence:**
  1. Identify all cards/entities in the current context.
  2. Activate all corresponding `tm-*` skills.
  3. Formulate and provide strategic advice based on the combined expert data.
- **Example:** When analyzing an "Initial Research Phase", you must load the skills for both Corporations, all 4 Preludes, and all 10 Project cards BEFORE giving any recommendations.
- **Goal:** Every piece of advice must be backed by the deep meta-data and synergy logic contained within the specialized skills.
