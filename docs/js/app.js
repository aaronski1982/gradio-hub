// Function to check if a URL is alive
async function checkURL(url) {
    try {
        const response = await fetch(url, { mode: 'no-cors' });
        return true;
    } catch (error) {
        return false;
    }
}

// Function to create a card for each URL
function createURLCard(url) {
    const card = document.createElement('div');
    card.className = 'bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow';
    
    const title = document.createElement('h2');
    title.className = 'text-xl font-semibold mb-2';
    title.textContent = url.name;
    
    const link = document.createElement('a');
    link.href = url.url;
    link.className = 'text-blue-600 hover:text-blue-800 break-all';
    link.textContent = url.url;
    
    const status = document.createElement('div');
    status.className = 'mt-4 flex items-center';
    status.innerHTML = `<span class="loading">Checking status...</span>`;
    
    if (url.description) {
        const description = document.createElement('p');
        description.className = 'text-gray-600 mt-2';
        description.textContent = url.description;
        card.appendChild(description);
    }
    
    card.appendChild(title);
    card.appendChild(link);
    card.appendChild(status);
    
    // Check URL status
    checkURL(url.url).then(isAlive => {
        status.innerHTML = isAlive 
            ? '<span class="text-green-600">🟢 Online</span>'
            : '<span class="text-red-600">🔴 Offline</span>';
    });
    
    return card;
}

// Function to load URLs from the JSON file
async function loadURLs() {
    try {
        const response = await fetch('urls.json');
        const urls = await response.json();
        const container = document.getElementById('links-container');
        
        if (urls.length === 0) {
            container.innerHTML = '<p class="text-gray-600">No URLs added yet.</p>';
            return;
        }
        
        urls.forEach(url => {
            container.appendChild(createURLCard(url));
        });
    } catch (error) {
        console.error('Error loading URLs:', error);
        document.getElementById('links-container').innerHTML = 
            '<p class="text-red-600">Error loading URLs. Please try again later.</p>';
    }
}

// Load URLs when the page loads
document.addEventListener('DOMContentLoaded', loadURLs); 