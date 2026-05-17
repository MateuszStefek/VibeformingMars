import yaml
import os
import re
import subprocess

CARDS_YML = 'cards.yml'
REPO_PATH = '.downloads/terraforming-mars'
CARDS_DIR = f'{REPO_PATH}/src/server/cards'

def to_snake_upper(name):
    s = re.sub(r'[^a-zA-Z0-9]', '_', name)
    return re.sub(r'_+', '_', s).upper()

def find_card_file(card_name):
    upper_name = to_snake_upper(card_name)
    pattern = f"name: CardName.{upper_name}"
    try:
        result = subprocess.run(['grep', '-r', '-l', pattern, CARDS_DIR], capture_output=True, text=True)
        files = result.stdout.strip().split('\n')
        return files[0] if files and files[0] else None
    except Exception:
        return None

def extract_data(file_path):
    if not file_path or not os.path.exists(file_path):
        return {}
    
    with open(file_path, 'r') as f:
        content = f.read()

    data = {}
    
    # Cost
    cost_match = re.search(r'cost:\s*(\d+)', content)
    if cost_match:
        data['cost'] = int(cost_match.group(1))
    else:
        super_match = re.search(r'super\s*\(\s*[^,]+,\s*(\d+)', content)
        if super_match:
            data['cost'] = int(super_match.group(1))
        else:
            mining_match = re.search(r'super\s*\(\s*name,\s*(\d+)', content)
            if mining_match:
                data['cost'] = int(mining_match.group(1))

    # Tags
    tags_match = re.search(r'tags:\s*\[(.*?)\]', content, re.DOTALL)
    if tags_match:
        tag_list = tags_match.group(1)
        tags = re.findall(r'Tag\.(\w+)', tag_list)
        if tags:
            data['tags'] = [t.lower() for t in tags]

    # Requirements
    req_list = []
    req_matches = re.findall(r'requirements:\s*(\[.*?\]|{.*?})', content, re.DOTALL)
    if req_matches:
        req_str = req_matches[0]
        is_max = 'max' in req_str
        
        found_any = False
        for key in ['oxygen', 'temperature', 'oceans', 'tr']:
            m = re.search(fr'{key}:\s*(-?\d+)', req_str)
            if m:
                item = {key: int(m.group(1))}
                if is_max:
                    item['max'] = True
                req_list.append(item)
                found_any = True
        
        for key in ['temperatureMin', 'temperatureMax']:
            m = re.search(fr'{key}:\s*(-?\d+)', req_str)
            if m:
                clean_key = key.replace('Min', '').replace('Max', '').lower()
                item = {clean_key: int(m.group(1))}
                if 'Max' in key:
                    item['max'] = True
                req_list.append(item)
                found_any = True

        tag_req_matches = re.findall(r'tag:\s*Tag\.(\w+)(?:,\s*count:\s*(\d+))?', req_str)
        for t_name, count in tag_req_matches:
            req_list.append({'tag': t_name.lower(), 'count': int(count) if count else 1})
            found_any = True
            
        if not found_any:
            req_list.append('other')

    # Implicit requirements (negative production)
    prod_match = re.search(r'production:\s*{(.*?)}', content, re.DOTALL)
    if prod_match:
        prod_str = prod_match.group(1)
        neg_prods = {}
        for res in ['energy', 'megacredits', 'steel', 'titanium', 'plants', 'heat']:
            m = re.search(fr'{res}:\s*-(\d+)', prod_str)
            if m:
                neg_prods[res] = int(m.group(1))
        if neg_prods:
            req_list.append({'production': neg_prods})

    if req_list:
        data['requirements'] = req_list

    # VP
    vp_match = re.search(r'victoryPoints:\s*(\d+)', content)
    if vp_match:
        data['vp'] = vp_match.group(1)
    else:
        vp_text_match = re.search(r"vpText:\s*'([^']+)'", content)
        if vp_text_match:
            data['vp'] = vp_text_match.group(1)
        else:
            vp_text_match = re.search(r"b\.vpText\('([^']+)'\)", content)
            if vp_text_match:
                data['vp'] = vp_text_match.group(1)

    # Starting Resources
    mc_match = re.search(r'startingMegaCredits:\s*(\d+)', content)
    if mc_match:
        data['startingMC'] = int(mc_match.group(1))
    
    # Description
    desc_match = re.findall(r"description:\s*'([^']+)'", content)
    if desc_match:
        data['description'] = desc_match[-1] # Take the one in metadata if possible
    return data

def main():
    if not os.path.exists(CARDS_YML):
        print(f"Error: {CARDS_YML} not found.")
        return

    with open(CARDS_YML, 'r') as f:
        cards_data = yaml.safe_load(f)

    updated_count = 0

    for category in ['corporations', 'preludes', 'projects']:
        for card in cards_data.get(category, []):
            file_path = find_card_file(card['name'])
            if file_path:
                new_data = extract_data(file_path)
                
                if 'cost' in new_data:
                    card['cost'] = new_data['cost']
                elif category == 'preludes' or category == 'corporations':
                    card['cost'] = 0
                
                if 'tags' in new_data:
                    card['tags'] = new_data['tags']
                else:
                    card['tags'] = []

                if 'vp' in new_data:
                    card['vp'] = str(new_data['vp'])
                elif 'vp' in card:
                    del card['vp']
                
                if 'requirements' in new_data:
                    card['requirements'] = new_data['requirements']
                elif 'requirements' in card:
                    del card['requirements']
                
                if 'description' in new_data:
                    card['description'] = new_data['description']
                
                updated_count += 1

    with open(CARDS_YML, 'w') as f:
        yaml.dump(cards_data, f, sort_keys=False, allow_unicode=True)

    print(f"Finished. Updated {updated_count} cards.")

if __name__ == "__main__":
    main()
