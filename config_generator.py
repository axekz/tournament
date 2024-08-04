import pandas as pd
import yaml

# Load the CSV file into a DataFrame
csv_path = 'players.csv'
players_df = pd.read_csv(csv_path)

# Load the configuration from config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Extract the base path from the configuration
base_path = config['base_path']

# Function to generate configuration entries for each player
def generate_config_entry(steamid, player_name):
    steamid_safe = steamid.replace(':', '_')
    
    icon_entry = f'''
        "{steamid_safe}"
        {{
            "class" "{steamid_safe}"
            "vmt" "materials/{base_path}{steamid_safe}.vmt"
            "vtf" "materials/{base_path}{steamid_safe}.vtf"
        }}
    '''
    
    player_entry = f'''
        "{steamid_safe}"
        {{
            "auth" "steam"
            "class" "{steamid_safe}"
            "attribute" "{steamid}"
            "scale" "0.4"
        }}
    '''
    
    return icon_entry, player_entry

# Generate the config content
icon_config = ''
player_config = ''

for index, row in players_df.iterrows():
    icon_entry, player_entry = generate_config_entry(row['STEAMID'], row['昵称'])
    icon_config += icon_entry
    player_config += player_entry

# Combine the configurations
final_config = f'''
"Icons"
{{
    "File"
    {{
{icon_config}
    }}
    "Player"
    {{
{player_config}
    }}
}}
'''

# Remove empty lines
final_config_lines = final_config.split('\n')
final_config_non_empty = [line for line in final_config_lines if line.strip() != '']
final_config_cleaned = '\n'.join(final_config_non_empty)

# Save the configuration to a file
config_path = 'icon.cfg'
with open(config_path, 'w') as file:
    file.write(final_config_cleaned)

print(f"Configuration file has been generated and saved to {config_path}")
