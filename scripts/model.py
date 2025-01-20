from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from scripts.config import columns_to_remove_model, model_path, scaler_path, player_data_path
from clean_data import clean_data
import pandas as pd 
import joblib 


def remove_columns(df, columns_to_remove_model):
    """Remove columns from the DataFrame."""

    return df.drop(columns=columns_to_remove_model, errors='ignore')

def normalize_data(X):
    """Normalize the data."""

    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)
    return X_normalized, scaler

def train_knn(X, n_neighbours=5):
    """Train the KNN model."""

    knn = NearestNeighbors(n_neighbors=n_neighbours, metric='euclidean')
    knn.fit(X)
    return knn

def save_model_and_scaler(model, scaler, player_data, model_path, scaler_path, player_data_path):
    """Saves the trained model, scaler, and player data to files."""
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    player_data.to_csv(player_data_path, index=False)
    print(f"Model saved to {model_path}")
    print(f"Scaler saved to {scaler_path}")
    print(f"Player data saved to {player_data_path}")

def build_save_models(df):
    """Build and save KNN model, scaler and player data"""

    df_cleaned = remove_columns(df, columns_to_remove_model)

    # Extracting features for model 
    X = df_cleaned.drop(columns=['Name']).values
    player_names = df_cleaned['Name'].values

    # Normalize the data
    X_normalized, scaler = normalize_data(X)

    # Combine normalized data with player names
    player_data = pd.DataFrame(X_normalized, columns=df_cleaned.columns.drop(['Name']))
    player_data.insert(0, 'Name', player_names)

    # Train KNN model 
    knn_model = train_knn(X_normalized, n_neighbours=5)

    # Save model, scaler and player data
    save_model_and_scaler(knn_model, scaler, player_data, model_path, scaler_path, player_data_path)


    
