document.addEventListener('DOMContentLoaded', function() {
    const groceryList = document.getElementById('grocery-list');
    const groceryForm = document.getElementById('grocery-form');
    const localStorageKey = 'groceryList';

    // Load from localStorage
    function loadGroceryList() {
        let storedList = JSON.parse(localStorage.getItem(localStorageKey)) || [];
        storedList.forEach(item => addItemToDOM(item));
    }

    // Save to localStorage
    function saveGroceryList(items) {
        localStorage.setItem(localStorageKey, JSON.stringify(items));
    }

    // Add item to the DOM
    function addItemToDOM(item) {
        const li = document.createElement('li');
        li.textContent = `${item.item} - ${item.quantity}`;
        groceryList.appendChild(li);
    }

    // Handle form submission
    groceryForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const item = document.getElementById('item').value;
        const quantity = document.getElementById('quantity').value;

        const groceryItem = { item, quantity };

        addItemToDOM(groceryItem);

        let storedList = JSON.parse(localStorage.getItem(localStorageKey)) || [];
        storedList.push(groceryItem);
        saveGroceryList(storedList);

        groceryForm.reset();
    });

    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/service-worker.js')
            .then(registration => {
                console.log('Service Worker registered with scope:', registration.scope);
            })
            .catch(error => {
                console.log('Service Worker registration failed:', error);
            });
    }
    
    // Initialize
    loadGroceryList();
});

