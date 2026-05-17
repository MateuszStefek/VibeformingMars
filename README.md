<p align="center">
  <img src="assets/logo.jpeg" width="300" alt="Vibeforming Mars Logo">
</p>

# 🪐 Vibeforming Mars

**Vibeforming Mars** is the definitive strategic library for *Terraforming Mars*, providing advanced AI agent skills built on the 2024–2025 competitive meta.

This repository is designed to be used with the **Gemini CLI** (or any agent supporting the [Agent Skills](https://agentskills.io) standard) to assist players with drafting decisions, engine optimization, and board-state management.

## 🚀 Key Features

- **Strategic Coverage:** Detailed analysis for all 208 Base Game project cards, 35 Preludes, and 54 official Corporations.
- **2025 Meta:** Insights derived from high-level play (Barena, Steam, and Discord communities).
- **Map Analysis:** Tailored advice for the **Tharsis**, **Hellas**, and **Elysium** boards.
- **Token Efficient:** Optimized formatting for fast agent response times and context management.

## 📂 Project Structure

Skills are located in the `.agents/skills/` directory using a flat structure for maximum compatibility:

- `tm-general-strategy/`: Foundation rules and resource management.
- `tm-project-[name]/`: Tactics for individual Project Cards.
- `tm-prelude-[name]/`: Jumpstart strategies for Prelude cards.
- `tm-corp-[name]/`: Comprehensive guides for each Corporation.

## 🔍 Examples

Explore the strategic library through these featured skills:

### 🏢 Corporations
- [**Point Luna**](.agents/skills/tm-corp-point-luna/SKILL.md) - The premier card-draw engine.
- [**Credicor**](.agents/skills/tm-corp-credicor/SKILL.md) - Mastering the standard project rush.
- [**UNMI**](.agents/skills/tm-corp-unmi/SKILL.md) - The high-skill terraforming specialist.

### 🎬 Preludes
- [**Ecology Experts**](.agents/skills/tm-prelude-ecology-experts/SKILL.md) - How to "cheat" out game-ending cards in Generation 1.
- [**Excentric Sponsor**](.agents/skills/tm-prelude-excentric-sponsor/SKILL.md) - Accelerating the tempo of your start.
- [**Allied Bank**](.agents/skills/tm-prelude-allied-bank/SKILL.md) - The gold standard of economic openings.

### 🃏 Project Cards
- [**Earth Catapult**](.agents/skills/tm-project-earth-catapult/SKILL.md) - The undisputed king of engine building.
- [**AI Central**](.agents/skills/tm-project-ai-central/SKILL.md) - The engine king of raw card volume.
- [**Underground Detonations**](.agents/skills/tm-project-underground-detonations/SKILL.md) - Tactical advice for the game's favorite meme card.

---

## 🛠 Usage

To use these skills with the Gemini CLI, simply point the agent to this repository. The agent will automatically discover the skills in the `.agents/skills/` folder and activate them when you ask questions about specific cards or strategies.
