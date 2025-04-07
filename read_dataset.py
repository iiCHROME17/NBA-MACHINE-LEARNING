import pandas as pd

games_df = pd.read_csv('dataset/NBA_GAMES.csv')
players_df = pd.read_csv('dataset/NBA_PLAYERS.csv')
teams_df = pd.read_csv('dataset/NBA_TEAMS.csv')
player_games_df = pd.read_csv('dataset/NBA_PLAYER_GAMES.csv')

# Clean up the dataframes:
# Remove any inactive players from the players_df, they are unnecessary for analysis
players_df = players_df[players_df['is_active'] == True]
player_games_df = player_games_df[player_games_df['Player_ID'].isin(players_df['Player_ID'])]

# Change game dates to datetime
games_df['GAME_DATE'] = pd.to_datetime(games_df['GAME_DATE'])