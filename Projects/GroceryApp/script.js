document.addEventListener('DOMContentLoaded', () => {
    fetchGroceryList();
    document.getElementById('add-item-form').addEventListener('submit', (event) => {
        event.preventDefault();
        addItem();
    });
});

function fetchGroceryList() {
    if (navigator.onLine) {
        fetch('http://localhost:8000')
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

    foodListElement.innerHTML = '';
    nonFoodListElement.innerHTML = '';

    data.food.forEach(item => {
        addItemToList('food', item.food, item.amount);
    });

    data.nonfood.forEach(item => {
        addItemToList('nonfood', item.item, item.amount);
    });
}

function addItemToList(category, item, amount) {
    const listElement = category === 'food' ? document.getElementById('food-list') : document.getElementById('nonfood-list');
    const li = document.createElement('li');
    li.textContent = `${item}: ${amount}`;
    listElement.appendChild(li);
}

function addItem() {
    const category = document.querySelector('input[name="category"]:checked').value;
    const item = document.getElementById('item').value;
    const quantity = document.getElementById('quantity').value;

    fetch('http://localhost:8000', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ category, g_item: item, amount: quantity })
    })
    .then(response => {
        if (response.ok) {
            // Add the new item to the page immediately
            addItemToList(category.toLowerCase(), item, quantity);
            document.getElementById('add-item-form').reset();
        } else {
            console.error('Error adding item');
        }
    })
    .catch(error => console.error('Error:', error));
}