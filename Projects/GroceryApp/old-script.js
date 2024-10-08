document.addEventListener('DOMContentLoaded', () => {
    fetchGroceryList();
    document.getElementById('add-item-form').addEventListener('submit', (event) => {
        event.preventDefault();  // Prevent default form submission behavior
        addItem();
    });
});

function fetchGroceryList() {
    fetch('http://localhost:8000')
        .then(response => response.json())
        .then(data => {
            displayGroceryList(data);
        })
        .catch(error => {
            console.error('Error fetching grocery list:', error);
        });
}

function displayGroceryList(data) {
    const foodListElement = document.getElementById('food-list');
    const nonFoodListElement = document.getElementById('nonfood-list');

    // Clear the existing content
    foodListElement.innerHTML = '';
    nonFoodListElement.innerHTML = '';

    if (data.food) {
        data.food.forEach(item => {
            addItemToList(foodListElement, item.food, item.amount);
        });
    }

    if (data.nonfood) {
        data.nonfood.forEach(item => {
            addItemToList(nonFoodListElement, item.item, item.amount);
        });
    }
}

function addItemToList(listElement, item, amount) {
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
            fetchGroceryList();  // Refresh the list to include the new item
            document.getElementById('item').value = '';
            document.getElementById('quantity').value = '';
        } else {
            console.error('Error adding item');
        }
    })
    .catch(error => console.error('Error:', error));
}
