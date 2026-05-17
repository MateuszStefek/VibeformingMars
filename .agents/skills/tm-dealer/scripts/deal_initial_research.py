import random
import os
import sys
import argparse
import yaml

# Add project root to sys.path to import local modules
sys.path.append(os.getcwd())
from scripts.tm_format import calculate_card_widths, render_card_row

def load_cards_registry():
    yml_path = os.path.join(os.getcwd(), 'cards.yml')
    if not os.path.exists(yml_path): return None
    with open(yml_path, 'r') as f: return yaml.safe_load(f)

def load_maps_registry():
    yml_path = os.path.join(os.getcwd(), 'maps.yml')
    if not os.path.exists(yml_path): return None
    with open(yml_path, 'r') as f: return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description='Terraforming Mars Card Dealer')
    parser.add_argument('num_players', type=int)
    parser.add_argument('--user-id', type=int, default=1)
    parser.add_argument('--variant', type=str, default="Base game")
    parser.add_argument('--other-expansions', type=str, default="")
    parser.add_argument('--map', type=str, default=None)
    
    args = parser.parse_args()
    
    maps_data = load_maps_registry()
    map_options = maps_data['maps'] if maps_data else []
    
    selected_map = None
    if args.map:
        for m in map_options:
            if m['name'].lower() == args.map.lower() or m['id'].lower() == args.map.lower() or args.map.lower() in m['name'].lower():
                selected_map = m
                break
    
    if not selected_map:
        print("\nSelect Map:")
        for i, m in enumerate(map_options):
            print(f"{i+1}. {m['name']}")
        
        map_choice = input(f"Enter choice (1-{len(map_options)}): ")
        try:
            selected_map = map_options[int(map_choice)-1]
        except:
            selected_map = map_options[0] # Default to Tharsis

    allowed = set(["Base Game (Basic)", "Base Game (Corporate Era)"])
    if "Prelude" in args.variant: 
        allowed.add("Prelude")
    if args.other_expansions:
        for e in args.other_expansions.split(','):
            # Try some common variants
            val = e.strip()
            allowed.add(val)
            allowed.add(val.capitalize())
            allowed.add(val.title())

    data = load_cards_registry()
    if not data: sys.exit(1)
    
    def fetch(cat): 
        return [c for c in data[cat] if c['expansion'] in allowed]
    
    corps = fetch('corporations')
    preludes = fetch('preludes')
    projects = fetch('projects')
    
    random.shuffle(corps)
    random.shuffle(preludes)
    random.shuffle(projects)
    
    print(f"\nMap: {selected_map['name']}")
    print(f"Milestones: {', '.join(selected_map['milestones'])}")
    print(f"Awards: {', '.join(selected_map['awards'])}")
    print(f"\nYou are player {args.user_id}.")
    print(f"Player {random.randint(1, args.num_players)} will start.")
    
    user_deal = {
        'corps': sorted([corps.pop() for _ in range(2)], key=lambda x: x['name']),
        'preludes': sorted([preludes.pop() for _ in range(4)], key=lambda x: x['name']) if "Prelude" in args.variant else [],
        'projects': sorted([projects.pop() for _ in range(10)], key=lambda x: x['name'])
    }
    
    widths = calculate_card_widths(user_deal['corps'] + user_deal['preludes'] + user_deal['projects'])
    
    print(f"\n### CORPORATIONS (Choose 1)")
    for c in user_deal['corps']: print(render_card_row(c, widths, show_cost=False))
    if user_deal['preludes']:
        print(f"\n### PRELUDES (Choose 2)")
        for p in user_deal['preludes']: print(render_card_row(p, widths, show_cost=False))
    print(f"\n### PROJECTS (Choose any number)")
    for p in user_deal['projects']: print(render_card_row(p, widths, show_cost=True))

if __name__ == "__main__":
    main()
