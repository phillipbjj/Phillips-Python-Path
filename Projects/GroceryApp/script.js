// Wait until the document is fully loaded before executing scripts
document.addEventListener('DOMContentLoaded', () => {
    fetchGroceryList(); // Fetch the grocery list from the server or localStorage

    // Add an event listener to the form to handle item submissions
    document.getElementById('add-item-form').addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the default form submission
        addItem(); // Add the new item to the grocery list
    });
});

// Function to fetch the grocery list, either from the server or from localStorage if offline
function fetchGroceryList() {
    if (navigator.onLine) { // Check if the user is online
        fetch('/grocerylist') // Make a GET request to the server to fetch the grocery list
            .then(response => response.json()) // Parse the response as JSON
            .then(data => {
                displayGroceryList(data); // Display the fetched grocery list
                storeGroceryListOffline(data); // Store the fetched data in localStorage for offline access
            })
            .catch(error => console.error('Error fetching grocery list:', error)); // Log any errors
    } else {
        fetchGroceryListOffline(); // If offline, fetch the list from localStorage
    }
}

// Function to store the grocery list in localStorage for offline access
function storeGroceryListOffline(data) {
    localStorage.setItem('groceryList', JSON.stringify(data)); // Convert the data to a JSON string and store it
}

// Function to fetch the grocery list from localStorage when offline
function fetchGroceryListOffline() {
    const storedData = localStorage.getItem('groceryList'); // Retrieve the data from localStorage
    if (storedData) { // Check if data exists in localStorage
        const data = JSON.parse(storedData); // Parse the JSON string back into an object
        displayGroceryList(data); // Display the grocery list
    } else {
        console.log('No data found in localStorage'); // Log a message if no data is found
    }
}

// Function to display the grocery list on the web page
function displayGroceryList(data) {
    const listElement = document.getElementById('grocery-list'); // Get the unordered list element by ID
    listElement.innerHTML = ''; // Clear any existing list items
    data.forEach(item => {
        const li = document.createElement('li'); // Create a new list item element
        li.textContent = `${item[1]}: ${item[2]}`; // Set the text content to the item name and quantity
        listElement.appendChild(li); // Append the list item to the unordered list
    });
}

// Function to add a new item to the grocery list
function addItem() {
    const item = document.getElementById('item').value; // Get the value from the item input field
    const quantity = document.getElementById('quantity').value; // Get the value from the quantity input field

    // Send a POST request to the server to add the new item
    fetch('/add', {
        method: 'POST', // Specify the request method as POST
        headers: {
            'Content-Type': 'application/json' // Set the request content type to JSON
        },
        body: JSON.stringify({ item, quantity }) // Convert the item and quantity to a JSON string
    })
    .then(response => {
        if (response.ok) { // Check if the response status is OK
            fetchGroceryList(); // Refresh the grocery list to include the new item
            document.getElementById('add-item-form').reset(); // Reset the form fields
        } else {
            console.error('Error adding item'); // Log an error if the response status is not OK
        }
    })
    .catch(error => console.error('Error:', error)); // Log any errors that occur during the fetch
}
