# app/routes.py

from flask import Blueprint, render_template, Flask, request, jsonify
from .recommendation.data_processing import fetch_songs_from_api, extract_audio_features, preprocess_data, normalize_data, save_data_to_database

bp = Blueprint('routes_bp', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/data_collection_and_preprocessing')
def data_collection_and_preprocessing():
    # Define my API endpoint
    api_endpoint = 'https://api.spotify.com/v1/me/tracks'

    # Step 1: Fetch songs dataset using an API
    songs_dataset = fetch_songs_from_api(api_endpoint)

    # Step 2: Extract relevant audio features
    audio_features = extract_audio_features(songs_dataset)

    # Step 3: Preprocess the dataset
    preprocessed_data = preprocess_data(audio_features)

    # Step 4: Normalize and scale audio features
    normalized_data = normalize_data(preprocessed_data)

    # Step 5: Save the preprocessed dataset for future use
    table_name = 'preprocessed_data_table'
    save_data_to_database(normalized_data, table_name)

    return "Data collection and preprocessing completed!"

# Assume playlists is a list or dictionary containing playlist data
playlists = {
    'playlist1': ['song1', 'song2', 'song3'],
    'playlist2': ['song4', 'song5'],
    # ...
}

# Route to edit a playlist
@bp.route('/api/playlists/<playlist_name>', methods=['PUT'])
def edit_playlist(playlist_name):
    try:
        # Get the new playlist name from the request JSON
        new_name = request.json['newName']
        
        # Update the playlist name
        playlists[new_name] = playlists.pop(playlist_name)
        
        return jsonify({'message': 'Playlist edited successfully'}), 200
    except KeyError:
        return jsonify({'error': 'New playlist name not provided in the request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a playlist
@bp.route('/api/playlists/<playlist_name>', methods=['DELETE'])
def delete_playlist(playlist_name):
    try:
        # Delete the playlist
        del playlists[playlist_name]
        
        return jsonify({'message': 'Playlist deleted successfully'}), 200
    except KeyError:
        return jsonify({'error': f'Playlist "{playlist_name}" not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
