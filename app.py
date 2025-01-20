import os
import joblib
import pandas as pd
import sys
from rapidfuzz import process  
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))

from scripts.model import build_save_models
from scripts.read_data import read_data
from scripts.clean_data import clean_data
from scripts.config import model_path, scaler_path, player_data_path

def load_model_and_data():
    if os.path.exists(model_path) and os.path.exists(scaler_path) and os.path.exists(player_data_path):
        print("Loading existing model, scaler, and player data")
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        player_data = pd.read_csv(player_data_path)

    else:
        print("Building and saving model, scaler, and player data")
        main_df, fifa_df = read_data()
        if main_df is None or fifa_df is None:
            raise FileNotFoundError("Data file missing or could not be read")
        
        # clean data 
        cleaned_df = clean_data(main_df, fifa_df)

        # build and save model 
        build_save_models(cleaned_df)

        # reload saved components 
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        player_data = pd.read_csv(player_data_path)

    return model, scaler, player_data

def find_similar_players(model, scaler, player_data, n_recommendations=5):
    while True:
        player_name = input("Enter a player name: ")

        # Check if the player name exists exactly in the dataset
        if player_name in player_data['Name'].values:
            # Get the player's data
            player_row = player_data[player_data['Name'] == player_name]
            player_stats = player_row.drop(columns=['Name']).values

            # Find similar players
            distances, indices = model.kneighbors(player_stats, n_neighbors=n_recommendations + 1)

            # Return the similar players
            similar_players = player_data.iloc[indices[0][1:]]
            similar_players['Distance'] = distances[0][1:]  # Add distances

            return similar_players
        else:
            # Use fuzzy matching to find the closest match
            closest_matches = process.extract(player_name, player_data['Name'].values, limit=3)
            
            # Display suggestions to the user
            print(f"Player '{player_name}' not found in the dataset. Did you mean:")
            for i, (match, score, _) in enumerate(closest_matches, start=1):
                print(f"{i}. {match} (Score: {score:.2f})")
            
            try:
                choice = int(input("Enter the number of the correct player, or 0 to try again: "))
                if choice == 0:
                    continue  # Ask for input again
                elif 1 <= choice <= len(closest_matches):
                    selected_player = closest_matches[choice - 1][0]
                    print(f"Using player: {selected_player}")
                    player_row = player_data[player_data['Name'] == selected_player]
                    player_stats = player_row.drop(columns=['Name']).values

                    # Find similar players
                    distances, indices = model.kneighbors(player_stats, n_neighbors=n_recommendations + 1)

                    # Return the similar players
                    similar_players = player_data.iloc[indices[0][1:]]
                    similar_players['Distance'] = distances[0][1:]  # Add distances

                    return similar_players
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    model, scaler, player_data = load_model_and_data()
    try:
        recommendations = find_similar_players(model, scaler, player_data)
        print(f"Top 5 simliar players are: \n{recommendations}")
        print(recommendations[['Name', 'Distance']])

    except ValueError as e:
        print(e)