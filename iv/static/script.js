// Toggle dropdown menu visibility when clicking the "Intravenous Access" button
document.getElementById('iv-access-btn').onclick = function() {
    var dropdown = document.getElementById('dropdown');
    dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
};

// Function to save the selected intravenous access type to the database
function saveAccess(accessType) {
    fetch('/save', {
        method: 'POST',  // Use POST method for sending data
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',  // Define content type for the request
        },
        body: 'access_type=' + accessType  // Send the selected access type as data in the request body
    })
    .then(response => response.json())  // Parse the response as JSON
    .then(data => {
        // Display the success message
        document.getElementById('message').innerText = data.message;
        displayData();  // After saving, refresh the data display
    });
}

// Function to fetch and display saved data (the list of intravenous access types)
function displayData() {
    fetch('/data')  // Send GET request to fetch the stored access types
        .then(response => response.json())  // Parse the JSON response
        .then(data => {
            // Create an unordered list to display the saved data
            let output = '<ul>';
            data.forEach(row => {
                output += `<li>${row[1]}</li>`;  // row[1] contains the access type
            });
            output += '</ul>';
            document.getElementById('data-display').innerHTML = output;  // Display the list inside the "data-display" div
        });
}

// Initial call to display any existing data when the page loads
displayData();
