import os
import pandas as pd
import yaml

# Load the configuration from config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Extract the base path and VMT template from the configuration
base_path = config['base_path']
vmt_template = '''"UnlitGeneric"
{{
    "$basetexture" "{base_path}{steamid_safe}"
    "$translucent" 1
    "$decal" "1"
    "$decalscale" "0.15"
    "$selfillum" 1
}}
'''
# Load the CSV file into a DataFrame
csv_path = 'players.csv'
players_df = pd.read_csv(csv_path)

# Ensure the base path directory exists
materials_path = os.path.join('materials', base_path)
os.makedirs(materials_path, exist_ok=True)

# Function to generate .vmt file content for each player
def generate_vmt_content(steamid):
    steamid_safe = steamid.replace(':', '_')
    return vmt_template.format(base_path=base_path, steamid_safe=steamid_safe)

# Generate .vmt files for each player
for index, row in players_df.iterrows():
    steamid = row['STEAMID']
    steamid_safe = steamid.replace(':', '_')
    vmt_content = generate_vmt_content(steamid)
    vmt_filename = f'{steamid_safe}.vmt'
    vmt_filepath = os.path.join(materials_path, vmt_filename)
    
    with open(vmt_filepath, 'w') as vmt_file:
        vmt_file.write(vmt_content)

print(f".vmt files have been generated and saved to {materials_path}")
