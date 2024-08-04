from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Load the CSV file into a DataFrame
csv_path = 'players.csv'
# Path to the PingFang TTC font file
font_path = "/Users/cinyan10/Documents/fonts/PingFang.ttc"
players_df = pd.read_csv(csv_path)

def create_image_with_text(player_name, team_name, steamid, text_color="#F2FF00"):
    # Image size
    width, height = 500, 500
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Define the font and size
    try:
        # Load the font with index 0 (the first font in the collection)
        font = ImageFont.truetype(font_path, 40, index=0)
    except IOError:
        raise Exception("Font file not found. Please provide a valid path to a TrueType Collection font file.")

    # Calculate the position for the team name
    team_text_bbox = draw.textbbox((0, 0), player_name, font=font)
    team_text_width, team_text_height = team_text_bbox[2] - team_text_bbox[0], team_text_bbox[3] - team_text_bbox[1]
    team_text_x = (width - team_text_width) / 2
    team_text_y = height * 0.4 - team_text_height / 2  # Ensure the text is above the halfway point

    # Calculate the position for the player name
    player_text_bbox = draw.textbbox((0, 0), team_name, font=font)
    player_text_width, player_text_height = player_text_bbox[2] - player_text_bbox[0], player_text_bbox[3] - player_text_bbox[1]
    player_text_x = (width - player_text_width) / 2
    player_text_y = team_text_y - team_text_height - 20  # Position above the team name

    # Draw the team name
    draw.text((team_text_x, team_text_y), player_name, font=font, fill=text_color)
    
    # Draw the player name
    draw.text((player_text_x, player_text_y), team_name, font=font, fill=text_color)

    # Save the image to a file
    file_name = steamid.replace(':', '_')
    image.save(f"img/{file_name}.png", "PNG")

if __name__ == '__main__':
    for index, row in players_df.iterrows():
        create_image_with_text(row['昵称'], row['Team Name'], row['STEAMID'], text_color=row['Color'])