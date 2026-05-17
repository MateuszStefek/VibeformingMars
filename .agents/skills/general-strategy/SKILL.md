---
name: tm-general-strategy
description: Provides foundational knowledge and strategic heuristics for Terraforming Mars. Use this when analyzing game state or resource management.
---

# Terraforming Mars: General Strategy

## Core Resources
- **MegaCredits (MC):** Primary currency for playing cards and standard projects.
- **Steel:** Can be used to pay for Building tags (value: 2 MC per steel).
- **Titanium:** Can be used to pay for Space tags (value: 3 MC per titanium).
- **Plants:** 8 plants = 1 Greenery tile (increases TR and Oxygen).
- **Energy:** Converted to Heat at the end of the generation. Used for certain card requirements and oxygen production.
- **Heat:** 8 heat = 1 Temperature step (increases TR).

## Strategic Priorities
1. **Engine Building (Early Game):** Focus on increasing MC production and resource efficiency.
2. **Terraforming (Late Game):** Push global parameters (Oxygen, Temperature, Oceans) to increase TR and end the game.
3. **Milestones and Awards:** Monitor progress towards milestones (e.g., Builder, Mayor) as they are high-value point sources.
4. **Card Synergy:** Prioritize cards with tags that match your existing engine (e.g., Space, Science, Plant).
5. **Efficiency & Timing:** DO NOT play a card until you can derive benefit from it. Playing a card prematurely is "dead capital" that reduces your flexibility to react to high-impact cards in the draft.
6. **Flexibility (Liquid Capital):** Maintain a reserve of MC. Liquid capital is more valuable than cards in play that aren't yet active.
7. **Map-Specific Strategy:** ALWAYS identify the map (Tharsis, Hellas, Elysium) before committing to a strategy. Milestones and Awards vary significantly by map and should dictate your long-term goals. Consult the corresponding `tm-map-<id>` skill for detailed tips.

## Rules Compliance Mandate
- **Requirement Check:** ALWAYS cross-reference a card's global requirements (Oxygen, Temperature, Oceans) and tag requirements BEFORE suggesting it as a viable play.
- **Generation 1 Limitations:** Pay extreme attention to requirements in the opening generation. Most powerful cards cannot be played Gen 1 unless a Corporation or Prelude provides the necessary tags or global parameter bumps.
- **Cost vs. Value:** Ensure the player has enough MC (including resource conversions like Steel/Titanium) to actually afford the suggested play sequence.
- **Dependency Verification:** Before recommending a card with an active ability (Action), verify that the player has the necessary production or resources to actually USE that action in the same or next generation (e.g., verify Energy production before playing 'Martian Rails').
- **Map Context:** Check for map-specific placement bonuses (e.g., Olympus Mons card draw on Elysium) when suggesting tile placements.

## Rule Nuances
- **Tag Requirements:** You must have the required number of tags *already in play* (not including the tags on the card you are currently playing) to play a card.
- **Production Requirements:** If a card specifies "Decrease YOUR [resource] production," you MUST have at least that much production to play the card. This is effectively an additional requirement.
- **Global Parameter 'Max':** Cards with a "max" requirement (e.g., "max 3 oceans") cannot be played once that parameter has exceeded the limit.
- **Titanium/Steel:** Titanium can only be used for Space tags (🚀). Steel can only be used for Building tags (🏠).
- **Events (Red Cards):** Tags on Event cards only count *while they are being played*. They do not count as tags in play for future requirements.