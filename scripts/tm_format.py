import os
import sys

# Ensure local scripts are importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tm_ui import get_visual_width, pad_to_width

TAG_EMOJIS = {
    "building": "🏠",
    "space": "🚀",
    "power": "⚡",
    "science": "🧪",
    "earth": "🌍",
    "jovian": "🪐",
    "venus": "♀",
    "plant": "🌿",
    "microbe": "🦠",
    "animal": "🐾",
    "event": "🔴",
    "city": "⬢",
    "wild": "🃏",
    "crime": "🔪",
    "moon": "🌙",
    "mars": "♂",
    "vp_shield": "🛡"
}

def get_tag_display(tag_name):
    """Returns the emoji for a tag, or the capitalized name if missing."""
    return TAG_EMOJIS.get(tag_name.lower(), tag_name.capitalize())

def format_tags_raw(tags):
    """Combines tag emojis into a single raw string."""
    if not tags: return ""
    return "".join(get_tag_display(t) for t in tags)

def format_requirement(req):
    """Formats a single requirement object into a readable string."""
    if isinstance(req, str):
        return req
    
    parts = []
    if 'tag' in req:
        count = req.get('count', 1)
        parts.append(f"{req['tag']} tag{'s' if count > 1 else ''}: {count}")
    
    for key in ['oxygen', 'temperature', 'oceans', 'tr']:
        if key in req:
            val = req[key]
            suffix = " max" if req.get('max') else ""
            if key == 'temperature':
                parts.append(f"{val}C{suffix}")
            elif key == 'oceans':
                parts.append(f"{val} ocean{'s' if val > 1 else ''}{suffix}")
            else:
                parts.append(f"{key}: {val}{suffix}")
                
    if 'production' in req:
        prod = req['production']
        prod_parts = [f"{v} {k}" for k, v in prod.items()]
        parts.append(f"prod: {', '.join(prod_parts)}")
        
    return ", ".join(parts) if parts else "other"

def format_requirements_list(reqs):
    """Combines a list of requirements into a single readable string."""
    if not reqs: return ""
    if isinstance(reqs, str): return reqs
    return "; ".join(format_requirement(r) for r in reqs)

def calculate_card_widths(cards):
    """Calculates absolute max cell widths for every column component across a list of cards."""
    widths = {'name': 0, 'cost_inner': 0, 'tags_inner': 0, 'vp_inner': 0, 'req_inner': 0}
    for c in cards:
        widths['name'] = max(widths['name'], get_visual_width(c.get('name', '')))
        widths['cost_inner'] = max(widths['cost_inner'], get_visual_width(str(c.get('cost', '?'))))
        
        tags_str = format_tags_raw(c.get('tags', []))
        widths['tags_inner'] = max(widths['tags_inner'], get_visual_width(tags_str))
        
        vp_val = str(c.get('vp', ''))
        if vp_val:
            if len(vp_val) > 15: vp_val = vp_val[:12] + "..."
            widths['vp_inner'] = max(widths['vp_inner'], get_visual_width(vp_val))
            
        req_val = format_requirements_list(c.get('requirements', []))
        widths['req_inner'] = max(widths['req_inner'], get_visual_width(req_val))
    return widths

def render_card_row(c, widths, show_cost=True):
    """Renders a single aligned card row based on pre-calculated widths."""
    # 1. NAME
    name_col = pad_to_width(c.get('name', ''), widths['name'])
    
    # 2. COST (or Ghost Padding)
    if show_cost:
        cost_inner = pad_to_width(str(c.get('cost', '?')), widths['cost_inner'], 'right')
        cost_col = f"({cost_inner}MC)"
    else:
        # Ghost padding: ( + widths + MC + )
        cost_col = " " * (widths['cost_inner'] + 4)
    
    # 3. TAGS
    tags_raw = format_tags_raw(c.get('tags', []))
    tags_col = f"[{pad_to_width(tags_raw, widths['tags_inner'])}]"
    
    # 4. VP
    vp_val = str(c.get('vp', ''))
    if widths['vp_inner'] > 0:
        if vp_val:
            if len(vp_val) > 15: vp_val = vp_val[:12] + "..."
            vp_inner = pad_to_width(vp_val, widths['vp_inner'])
            vp_col = f"{TAG_EMOJIS['vp_shield']} {vp_inner}"
        else:
            # Shield (1) + space (1) + inner
            vp_col = " " * (2 + widths['vp_inner'])
    else:
        vp_col = ""
    
    # 5. REQS
    req_val = format_requirements_list(c.get('requirements', []))
    if widths['req_inner'] > 0:
        if req_val:
            req_inner = pad_to_width(req_val, widths['req_inner'])
            req_col = f"{{{req_inner}}}"
        else:
            # Brackets (2) + inner
            req_col = " " * (2 + widths['req_inner'])
    else:
        req_col = ""
    
    desc = c.get('description', 'No description available.')
    
    # Assembly with fixed spacing
    parts = [name_col, cost_col, tags_col]
    if vp_col: parts.append(vp_col)
    if req_col: parts.append(req_col)
    
    metadata_line = "  ".join(parts)
    return f"{metadata_line}  | {desc}"
