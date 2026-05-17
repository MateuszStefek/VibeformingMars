---
name: tm-game-research
description: Instructions and workflows for researching Terraforming Mars game data by leveraging the official source code. Use this when you need to verify card data, expansion contents, game logic, or update Skill classifications based on empirical data from the repository.
---

# Terraforming Mars Game Research

This skill formalizes the process of using the official Terraforming Mars source code as the "Source of Truth" for game mechanics, card data, and expansion content.

## Setup

The source code must be maintained in the `.downloads/terraforming-mars` directory. **DO NOT delete this directory after use.**

```bash
# Initial clone if missing
mkdir -p .downloads && git clone https://github.com/terraforming-mars/terraforming-mars .downloads/terraforming-mars

# Update the repository
cd .downloads/terraforming-mars && git pull
```

## Repository Structure

Key directories for research:
- `src/common/cards/`: Common types, `CardName.ts`, and `Tag.ts`.
- `src/server/cards/`: Server-side card logic, organized by expansion folders.
  - `base/`: Base game project cards.
  - `corporation/`: Base game corporations.
  - `prelude/`, `prelude2/`, `venusNext/`, `colonies/`, `turmoil/`, `ares/`: Expansion-specific cards and corporations.
  - `promo/`: Promotional cards and corporations.
  - `pathfinders/`, `moon/`, `community/`, `starwars/`, `underworld/`: Fan-made or newer expansion sets.
- `src/server/cards/StandardCardManifests.ts`: The main registration file for base game and Corporate Era cards.
- `src/locales/`: Translation files (JSON) containing localized names and descriptions for all cards.

## Card Registry

A consolidated registry of all cards and corporations is maintained in `cards.yml` at the project root. This file maps card names to their skill names and expansion classifications.

**Structure:**
- `corporations`: List of corporations.
- `projects`: List of project cards.
- `preludes`: List of prelude cards.

**Each entry includes:**
- `name`: Readable name of the card.
- `skill-name`: The directory name in `.agents/skills/`.
- `expansion`: The expansion classification (e.g., "Moon", "Base Game (Basic)").

Use this file to quickly find which skill corresponds to a card without parsing individual Markdown files.

## Workflows
...
### 5. Maintaining the Registry
If you create new skills or update classifications, ensure `cards.yml` is updated to reflect these changes. This allows other agents (like the `tm-dealer`) to function correctly.

### 1. Identifying Expansion Content
To find which cards belong to a specific expansion, check the `*CardManifest.ts` file in the corresponding directory.

Example: `src/server/cards/venusNext/VenusCardManifest.ts`

### 2. Verifying Card Stats
Read the individual card file in `src/server/cards/<expansion>/<CardName>.ts`. 
- `startingResources`: Initial resources or production.
- `tags`: List of tags on the card.
- `requirements`: Global or local requirements to play.
- `onPlay`: Immediate effects.
- `onEffect`: Triggered effects.
- `action`: Available actions for the card.

### 3. Updating Skill Classifications
When updating skills in `.agents/skills/`, use the repository to verify the `Included in` section. 
- **Base Game (Basic)**: Part of `BASE_CARD_MANIFEST` in `StandardCardManifests.ts`.
- **Base Game (Corporate Era)**: Part of `CORP_ERA_CARD_MANIFEST` in `StandardCardManifests.ts`.
- **Expansions**: Part of their respective manifests.

### 4. Localization Research
If you need the exact text of a card (e.g., flavor text or translated name), check `src/locales/pl/` (or other language codes) for the relevant expansion JSON file.

## Best Practices
- **Empirical Evidence**: Always prefer reading the source code over general knowledge.
- **Context Efficiency**: Use `grep` to find specific card names or tags across the whole repository before reading files.
- **Validation**: When the user asks "How does X work?", find the implementation in the code to provide a definitive answer.
