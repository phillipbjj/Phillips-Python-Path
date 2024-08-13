document.addEventListener('DOMContentLoaded', () => {
    fetchGroceryList(); // Fetch the grocery list from the server or localStorage

    // Add event listener for form submission
    document.getElementById('add-item-form').addEventListener('submit', (event) => {
        event.preventDefault();
        addItem();
    });
});

function fetchGroceryList() {
    if (navigator.onLine) {
        fetch('/grocerylist')
            .then(response => response.json())
            .then(data => {
                displayGroceryList(data);
                storeGroceryListOffline(data);
            })
            .catch(error => console.error('Error fetching grocery list:', error));
    } else {
        fetchGroceryListOffline();
    }
}

function storeGroceryListOffline(data) {
    localStorage.setItem('groceryList', JSON.stringify(data));
}

function fetchGroceryListOffline() {
    const storedData = localStorage.getItem('groceryList');
    if (storedData) {
        const data = JSON.parse(storedData);
        displayGroceryList(data);
    } else {
        console.log('No data found in localStorage');
    }
}

function displayGroceryList(data) {
    const foodListElement = document.getElementById('food-list');
    const nonFoodListElement = document.getElementById('nonfood-list');

    // Clear any existing list items
    foodListElement.innerHTML = '';
    nonFoodListElement.innerHTML = '';

    // Display Food items
    data.food.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.food}: ${item.amount}`;
        foodListElement.appendChild(li);
    });

    // Display Non-food items
    data.nonfood.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.item}: ${item.amount}`;
        nonFoodListElement.appendChild(li);
    });
}

function addItem() {
    const category = document.querySelector('input[name="category"]:checked').value;
    const item = document.getElementById('item').value;
    const quantity = document.getElementById('quantity').value;

    fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ category, g_item: item, amount: quantity })
    })
    .then(response => {
        if (response.ok) {
            fetchGroceryList();
            document.getElementById('add-item-form').reset();
        } else {
            console.error('Error adding item');
        }
    })
    .catch(error => console.error('Error:', error));
}
