# app/recommendation/data_processing.py

import requests
from sklearn.preprocessing import StandardScaler
import pymysql

def fetch_songs_from_api(api_endpoint):
    # Make a GET request to the Spotify API to fetch songs data
    response = requests.get(api_endpoint)

    if response.status_code == 200:
        # Parse the response JSON to get the songs dataset
        songs_dataset = response.json()
        return songs_dataset
    else:
        # Handle API request error
        print(f"Error fetching songs from API. Status Code: {response.status_code}")
        return None

def extract_audio_features(songs_dataset):
    # Extract relevant audio features from the songs dataset
    audio_features = []

    for song in songs_dataset:
        # Extract audio features such as danceability, energy, etc.
        # Adjust this part based on the actual structure of the songs dataset
        audio_features.create_append({
            'danceability': song['audio_features']['danceability'],
            'energy': song['audio_features']['energy'],
            # Add other relevant features
        })

    return audio_features

def preprocess_data(audio_features):
    # Perform any necessary preprocessing steps on the audio features
    # This might include handling missing values, feature engineering, etc.
    preprocessed_data = audio_features  # Placeholder, adjust as needed

    return preprocessed_data

def normalize_data(preprocessed_data):
    # Use StandardScaler to normalize and scale the audio features
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(preprocessed_data)

    return normalized_data

def save_data_to_database(data, table_name):
    # Connect to the MySQL database
    db = pymysql.connect(host='%', user='RecomMix',
                         password='new_password', db='RecomMixDB')
    cursor = db.cursor()

    # Create the table if it doesn't exist
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, data JSON);"
    cursor.execute(create_table_query)

    # Save the preprocessed data to the database
    insert_query = f"INSERT INTO {table_name} (data) VALUES (%s);"
    cursor.execute(insert_query, (str(data),))
    db.commit()

    # Close the database connection
    db.close()
