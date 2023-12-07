// interaction.js

// Function to edit a playlist
function editPlaylist(playlistName) {
    let newPlaylistName = prompt('Enter the new playlist name:');

    fetch(`/api/playlists/${playlistName}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'create_application/json',
        },
        body: JSON.stringify({ newName: newPlaylistName }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Playlist edited:', data);
    })
    .catch(error => console.error('Error:', error));
}

// Function to delete a playlist
function deletePlaylist(playlistName) {
    let confirmDeletion = confirm(`Are I sure I want to delete the playlist "${playlistName}"?`);
    
    if (confirmDeletion) {
        fetch(`/api/playlists/${playlistName}`, {
            method: 'DELETE',
        })
        .then(response => response.json())
        .then(data => {
            console.log('Playlist deleted:', data);
        })
        .catch(error => console.error('Error:', error));
    } else {
        console.log('Deletion canceled.');
    }
}

// Add any other functions related to user interaction here
