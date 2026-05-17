---
name: tm-dealer
description: Randomizes the "Initial Research Phase" for Terraforming Mars, handling multi-player deals and starting player selection.
---

# Skill: TM Dealer

This skill handles the randomization of cards and turn order for the setup phase of the game.

## Workflows

### 1. Deal Initial Research Phase
Use the bundled Python script to generate a random deal based on selected variants and expansions.

**Interaction Mandate:**
- Always ask the user which game variant/expansions are enabled. Options:
  - **Base game without corporate era** (Only basic cards, all start with 1 prod)
  - **Base game** (Basic + Corporate Era cards, all start with 0 prod)
  - **Preludes** (Base + Corporate Era + Prelude cards)
  - **Other** (Provide custom text/expansions)
- When asking the user for the number of players, always provide explicit options for **2, 3, 4, and 5** players.
- Always ask the user which **Map** they are playing on (**Tharsis**, **Hellas**, **Elysium**).
- Sort all lists (**Corporations**, **Preludes**, **Projects**) alphabetically.
- Group the deal into explicit categories with the following instructions:
  - **### CORPORATIONS (Choose 1)**
  - **### PRELUDES (Choose 2)**
  - **### PROJECTS (Choose any number - must pay 3MC each)**
- Do **not** show "(Included in: [Expansion Name])" when displaying the cards in the initial deal.
- **PROHIBITION:** Do **NOT** provide strategic advice, "notes", or map-specific tips during the dealing phase. The deal must consist ONLY of the card lists and game setup data. Wait for a specific user prompt before offering strategy.
- **Always use a code block (` ``` `) to display the card lists** to preserve the fixed-width alignment provided by the Python script.

**Command:**
```bash
python3 .agents/skills/tm-dealer/scripts/deal_initial_research.py <num_players> --variant "<variant_name>" [--map "<map_name>"] [--other-expansions "<expansion_list>"] [--user-id <1-N>] [--show-all]
```

**Expansions Reference:**
- Base Game
- Prelude
- Venus Next
- Colonies
- Turmoil
- Promo


**Parameters:**
- `<num_players>`: Total number of players in the game.
- `--variant`: The game variant (e.g., "Base game", "Prelude").
- `--map`: Optional: The name of the map (e.g., "Tharsis", "Hellas", "Elysium"). Providing this avoids an interactive prompt.
- `--user-id`: The index of the current user (defaults to 1).
- `--show-all`: Optional flag to reveal all players' cards (useful for debugging or solo-multiplay).

## Logic
- Loads card data from the centralized `cards.yml` registry at the project root.
- Card data in `cards.yml` includes a `description` field containing the card's effect or ability, which is displayed in the deal output.
- Ensures every player receives a unique set of 2 Corporations, 4 Preludes, and 10 Projects.
- Randomly assigns a starting player from the total player count.
- Adheres to the privacy rule: only the user's cards are shown by default.
