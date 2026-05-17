import unicodedata

# 100% Fixed Semantic Mapping
# Standard emojis = 2 cells
# Expansion symbols = 1 cell
# Text = 1 cell
# No variation selectors allowed
FIXED_WIDTHS = {
    "🏠": 2, "🚀": 2, "⚡": 2, "🧪": 2, "🪐": 2, "🌿": 2, "🦠": 2, "🐾": 2, 
    "🔴": 2, "🃏": 2, "🔪": 2, "🌙": 2, "🌍": 2,
    "♀": 1, "♂": 1, "⬢": 1, "🛡": 1
}

def get_visual_width(s):
    """Calculates terminal cells based on a fixed semantic lookup table."""
    # Strip variation selectors
    s = s.replace('\ufe0f', '').replace('\ufe0e', '').replace('\u200d', '')
    
    width = 0
    for char in s:
        if char in FIXED_WIDTHS:
            width += FIXED_WIDTHS[char]
        elif ord(char) > 0xFFFF or unicodedata.east_asian_width(char) in ('W', 'F'):
            width += 2
        else:
            width += 1
    return width

def pad_to_width(s, target_width, align='left'):
    """Pads a string with spaces to reach a target visual cell width."""
    current_width = get_visual_width(s)
    diff = max(0, target_width - current_width)
    if align == 'left':
        return s + (" " * diff)
    elif align == 'right':
        return (" " * diff) + s
    elif align == 'center':
        left_pad = " " * (diff // 2)
        right_pad = " " * (diff - len(left_pad))
        return left_pad + s + right_pad
    return s
