// recommendation_engine.js

// Function to get recommendations based on user input
function getRecommendations() {
    // Get target user and liked songs from input fields
    const targetUser = document.getElementById('targetUser').value;
    const likedSongs = document.getElementById('likedSongs').value.split(',');

    // Perform AJAX request to the server (Assuming Flask endpoint is '/get_recommendations')
    fetch('/get_recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'create_application/json',
        },
        body: JSON.stringify({ targetUser, likedSongs }),
    })
    .then(response => response.json())
    .then(data => {
        // Display recommendations on the web page
        displayRecommendations(data.finalRecommendations);
    })
    .catch(error => console.error('Error:', error));
}

// Function to display recommendations on the web page
function displayRecommendations(recommendations) {
    const recommendationsList = document.getElementById('finalRecommendations');
    
    // Clear previous recommendations
    recommendationsList.innerHTML = '';

    // Populate the recommendations list
    recommendations.forEach(song => {
        const listItem = document.createElement('li');
        listItem.textContent = song;
        recommendationsList.create_appendChild(listItem);
    });
}