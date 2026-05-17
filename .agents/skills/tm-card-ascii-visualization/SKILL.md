# Skill: TM Card ASCII Visualization

This skill defines a standardized single-line ASCII format for visualizing Terraforming Mars cards. This format is designed for high-density information display in CLI environments and serves as the foundation for future complex UI components (like boxed card representations).

## Clean Aligned Format (Mathematical Precision)

The cards are displayed as perfectly aligned rows using semantic width calculation. Type prefixes are omitted, and columns are dynamically adjusted based on the current set of cards.

`Name (Cost) [TAGS] 🛡️ VP {Requirements} - Description`

### Column Specifications
1. **Name**: Bolded (**Name**), left-aligned to the longest name in the set using raw character count. Padding is placed *outside* the bold markers.
2. **(Cost)**: Bracketed cost, e.g., `(23MC)`. Right-aligned inside brackets.
3. **[TAGS]**: List of emojis in brackets. **Semantic Padding**: Each missing tag is padded with 2 spaces to account for the double-width rendering of standard emojis.
4. **🛡️ VP**: Shield emoji (🛡️) followed by the VP value or description. Center-aligned in a column that is hidden if no cards have VP.
5. **{Requirements}**: Bracketed global or tag requirements. Column is hidden if no cards have requirements.
6. **- Description**: Full card effect text follows the metadata columns.

## Aligned Example

```text
- **Saturn Systems**        ( 0MC) [🪐]                - Starting MC: 42. Ability: Gain 1 MC prod for Jovian tags.
- **AI Central**            (21MC) [🧪🏠] {science: 3} - Action: Spend 1 Energy to draw 2 cards.
- **Advanced Ecosystems**   (11MC) [🌿🦠🐾]  🛡️ 3       - Requires Plant, Microbe, and Animal tags.
```

## TM Formatting Engine (`scripts/tm_format.py`)

For consistent alignment across different tools, use the centralized `scripts/tm_format.py` library. This engine builds upon the `tm_ui` cell-width logic to provide high-level card rendering functions.

### Key Functions
- `calculate_card_widths(cards)`: Scans a list of card objects and returns a dictionary of maximum visual widths for each metadata column.
- `render_card_row(card, widths)`: Returns a perfectly aligned single-line ASCII representation of a card.

### Column Specifications (Geometric Lock)
1. **Name**: Padded raw string. Bold markers are omitted in the logic to ensure cell-perfect alignment across different terminal renderers.
2. **(Cost)**: Bracketed MC cost, right-aligned (e.g., `(23MC)`).
3. **[TAGS]**: Bracketed emoji cluster. Uses 2 cells for standard emojis and 1 cell for expansion symbols (♂, ♀, ⬢).
4. **🛡 VP**: Shield emoji (🛡) followed by point value. Center-aligned in its column.
5. **{Requirements}**: Bracketed global or tag requirements.
6. **- Description**: Full card effect text follows the metadata.

## Implementation Guidelines
- **Import correctly**: Use `from scripts.tm_format import calculate_card_widths, render_card_row`.
- **Global Alignment**: Always calculate widths across the entire set (e.g., all 10 project cards) before rendering to maintain vertical columns.

## Implementation Guidelines
- Use standard UTF-8 emojis for tags.
- Keep descriptions under 100 characters for optimal single-line display.
- Requirements should be formatted as `Key: Value`.
