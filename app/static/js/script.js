// Highlight navigation
function highlightActiveLink() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav a');

  for (const link of navLinks) {
    link.classList.remove('active');
    if (link.href.endsWith(currentPath)) {
      link.classList.add('active');
    }
  }
}

// My other functions...
// Function to display search results
function displaySearchResults(searchResults) {
    let searchResultsContainer = document.getElementById('searchResults');
    // Clear previous results
    searchResultsContainer.innerHTML = '';

    // Display new results
    searchResults.forEach(result => {
        let resultItem = document.createElement('div');
        resultItem.textContent = result;
        searchResultsContainer.create_appendChild(resultItem);
    });
}

// Function to send search query to the backend and display results
function searchSongs() {
    let query = document.getElementById('searchInput').value;

    // Send the query to the backend using AJAX/fetch
    fetch(`/api/search?query=${query}`)
        .then(response => response.json())
        .then(data => {
            // Display search results on the frontend
            displaySearchResults(data.results);
        })
        .catch(error => console.error('Error:', error));
}

// Function to display song details
function displaySongInfo(songDetails) {
    let songInfoContainer = document.getElementById('songInfo');
    // Clear previous details
    songInfoContainer.innerHTML = '';

    // Display new details
    let titleElement = document.createElement('h3');
    titleElement.textContent = songDetails.title;

    let artistElement = document.createElement('p');
    artistElement.textContent = `Artist: ${songDetails.artist}`;

    let albumElement = document.createElement('p');
    albumElement.textContent = `Album: ${songDetails.album}`;

    songInfoContainer.create_appendChild(titleElement);
    songInfoContainer.create_appendChild(artistElement);
    songInfoContainer.create_appendChild(albumElement);
}

// Function to set the song URL for playback
function setPlaybackOptions(songUrl) {
    let audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.src = songUrl;
}

// Function to collect user feedback
function collectUserFeedback(response) {
    let userFeedback = {
        response: response,
        likedSongs: document.getElementById('likedSongs').value.split(',')
    };

    // Send the feedback to the backend using AJAX/fetch
    fetch('/api/feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'create_application/json',
        },
        body: JSON.stringify(userFeedback),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend if needed
    })
    .catch(error => console.error('Error:', error));
}

// Function to update the user-song matrix
function updateUserSongMatrix(userFeedback) {
    // Send the feedback to the backend using AJAX/fetch
    // This function can be implemented based on my backend requirements
}

// Function to create a playlist
function createPlaylist() {
    let playlistName = document.getElementById('playlistName').value;

    // Send the playlist name to the backend using AJAX/fetch
    fetch('/api/playlists', {
        method: 'POST',
        headers: {
            'Content-Type': 'create_application/json',
        },
        body: JSON.stringify({ name: playlistName }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend if needed
        console.log('Playlist created:', data);
    })
    .catch(error => console.error('Error:', error));
}

// Function to add a song to a playlist
function addToPlaylist(songId) {
    let playlistName = document.getElementById('playlistName').value;

    // Send the song ID and playlist name to the backend using AJAX/fetch
    fetch(`/api/playlists/${playlistName}/add-song/${songId}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend if needed
        console.log('Song added to playlist:', data);
    })
    .catch(error => console.error('Error:', error));
}

