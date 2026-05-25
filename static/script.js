// Tab Navigation
document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const tabName = btn.dataset.tab;
        
        // Remove active class from all buttons and sections
        document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(s => s.classList.remove('active'));
        
        // Add active class to clicked button and corresponding section
        btn.classList.add('active');
        document.getElementById(tabName).classList.add('active');
        
        // Load data for the section
        loadData(tabName);
    });
});

// Show Message
function showMessage(message, isError = false) {
    const toast = document.getElementById('message-toast');
    toast.textContent = message;
    toast.classList.remove('error');
    if (isError) toast.classList.add('error');
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Load Data
function loadData(section) {
    if (section === 'buses') loadBuses();
    else if (section === 'drivers') loadDrivers();
    else if (section === 'passengers') loadPassengers();
    else if (section === 'tickets') loadTickets();
}

// ==================== BUS FUNCTIONS ====================

document.getElementById('bus-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const bus = {
        plate_number: document.getElementById('bus-plate').value,
        brand: document.getElementById('bus-brand').value,
        model: document.getElementById('bus-model').value,
        color: document.getElementById('bus-color').value,
        year: document.getElementById('bus-year').value
    };
    
    try {
        const response = await fetch('/api/buses', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(bus)
        });
        
        if (response.ok) {
            showMessage('Bus added successfully!');
            document.getElementById('bus-form').reset();
            loadBuses();
        } else {
            showMessage('Error adding bus', true);
        }
    } catch (error) {
        showMessage('Error: ' + error.message, true);
    }
});

async function loadBuses() {
    try {
        const response = await fetch('/api/buses');
        const buses = await response.json();
        const container = document.getElementById('buses-list');
        container.innerHTML = '';
        
        if (buses.length === 0) {
            container.innerHTML = '<p style="text-align: center; color: #999;">No buses added yet</p>';
            return;
        }
        
        buses.forEach(bus => {
            container.innerHTML += `
                <div class="list-item">
                    <div class="item-details">
                        <div class="item-field"><strong>Plate:</strong> ${bus.plate_number}</div>
                        <div class="item-field"><strong>Brand:</strong> ${bus.brand} ${bus.model}</div>
                        <div class="item-field"><strong>Color:</strong> ${bus.color} | <strong>Year:</strong> ${bus.year}</div>
                    </div>
                    <div class="item-actions">
                        <button class="btn-danger" onclick="deleteBus(${bus.id})">Delete</button>
                    </div>
                </div>
            `;
        });
    } catch (error) {
        showMessage('Error loading buses', true);
    }
}

async function deleteBus(id) {
    if (!confirm('Delete this bus?')) return;
    try {
        const response = await fetch(`/api/buses/${id}`, { method: 'DELETE' });
        if (response.ok) {
            showMessage('Bus deleted successfully!');
            loadBuses();
        } else {
            showMessage('Error deleting bus', true);
        }
    } catch (error) {
        showMessage('Error: ' + error.message, true);
    }
}

// ==================== DRIVER FUNCTIONS ====================

document.getElementById('driver-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const driver = {
        nin: document.getElementById('driver-nin').value,
        first_name: document.getElementById('driver-first-name').value,
        last_name: document.getElementById('driver-last-name').value,
        driver_license: document.getElementById('driver-license').value,
        age: document.getElementById('driver-age').value,
        gender: document.getElementById('driver-gender').value
    };
    
    try {
        const response = await fetch('/api/drivers', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(driver)
        });
        
        if (response.ok) {
            showMessage('Driver added successfully!');
            document.getElementById('driver-form').reset();
            loadDrivers();
        } else {
            showMessage('Error adding driver', true);
        }
    } catch (error) {
        showMessage('Error: ' + error.message, true);
    }
});

async function loadDrivers() {
    try {
        const response = await fetch('/api/drivers');
        const drivers = await response.json();
        const container = document.getElementById('drivers-list');
        container.innerHTML = '';
        
        if (drivers.length === 0) {
            container.innerHTML = '<p style="text-align: center; color: #999;">No drivers added yet</p>';
            return;
        }
        
        drivers.forEach(driver => {
            container.innerHTML += `
                <div class="list-item">
                    <div class="item-details">
                        <div class="item-field"><strong>Name:</strong> ${driver.first_name} ${driver.last_name}</div>
                        <div class="item-field"><strong>NIN:</strong> ${driver.nin} | <strong>License:</strong> ${driver.driver_license}</div>
                        <div class="item-field"><strong>Age:</strong> ${driver.age} | <strong>Gender:</strong> ${driver.gender}</div>
                    </div>
                    <div class="item-actions">
                        <button class="btn-danger" onclick="deleteDriver(${driver.id})">Delete</button>
                    </div>
                </div>
            `;
        });
    } catch (error) {
        showMessage('Error loading drivers', true);
    }
}

async function deleteDriver(id) {
    if (!confirm('Delete this driver?')) return;
    try {
        const response = await fetch(`/api/drivers/${id}`, { method: 'DELETE' });
        if (response.ok) {
            showMessage('Driver deleted successfully!');
            loadDrivers();
        } else {
            showMessage('Error deleting driver', true);
        }
    } catch (error) {
        showMessage('Error: ' + error.message, true);
    }
}

// ==================== PASSENGER FUNCTIONS ====================

document.getElementById('passenger-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const passenger = {
        first_name: document.getElementById('passenger-first-name').value,
        last_name: document.getElementById('passenger-last-name').value,
        age: document.getElementById('passenger-age').value,
        gender: document.getElementById('passenger-gender').value,
        luggage_weight: document.getElementById('passenger-luggage').value
    };
    
    try {
        const response = await fetch('/api/passengers', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(passenger)
        });
        
        if (response.ok) {
            showMessage('Passenger added successfully!');
            document.getElementById('passenger-form').reset();
            loadPassengers();
        } else {
            showMessage('Error adding passenger', true);
        }
    } catch (error) {
        showMessage('Error: ' + error.message, true);
    }
});

async function loadPassengers() {
    try {
        const response = await fetch('/api/passengers');
        const passengers = await response.json();
        const container = document.getElementById('passengers-list');
        container.innerHTML = '';
        
        if (passengers.length === 0) {
            container.innerHTML = '<p style="text-align: center; color: #999;">No passengers added yet</p>';
            return;
        }
        
        passengers.forEach(passenger => {
            container.innerHTML += `
                <div class="list-item">
                    <div class="item-details">
                        <div class="item-field"><strong>Name:</strong> ${passenger.first_name} ${passenger.last_name}</div>
                        <div class="item-field"><strong>Age:</strong> ${passenger.age} | <strong>Gender:</strong> ${passenger.gender}</div>
                        <div class="item-field"><strong>Luggage Weight:</strong> ${passenger.luggage_weight} kg</div>
                    </div>
                    <div class="item-actions">
                        <button class="btn-danger" onclick="deletePassenger(${passenger.id})">Delete</button>
                    </div>
                </div>
            `;
        });
    } catch (error) {
        showMessage('Error loading passengers', true);
    }
}

async function deletePassenger(id) {
    if (!confirm('Delete this passenger?')) return;
    try {
        const response = await fetch(`/api/passengers/${id}`, { method: 'DELETE' });
        if (response.ok) {
            showMessage('Passenger deleted successfully!');
            loadPassengers();
        } else {
            showMessage('Error deleting passenger', true);
        }
    } catch (error) {
        showMessage('Error: ' + error.message, true);
    }
}

// ==================== TICKET FUNCTIONS ====================

document.getElementById('ticket-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const ticket = {
        departure_terminal: document.getElementById('ticket-departure').value,
        arrival_terminal: document.getElementById('ticket-arrival').value,
        age: document.getElementById('ticket-age').value
    };
    
    try {
        const response = await fetch('/api/tickets', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(ticket)
        });
        
        if (response.ok) {
            showMessage('Ticket added successfully!');
            document.getElementById('ticket-form').reset();
            loadTickets();
        } else {
            showMessage('Error adding ticket', true);
        }
    } catch (error) {
        showMessage('Error: ' + error.message, true);
    }
});

async function loadTickets() {
    try {
        const response = await fetch('/api/tickets');
        const tickets = await response.json();
        const container = document.getElementById('tickets-list');
        container.innerHTML = '';
        
        if (tickets.length === 0) {
            container.innerHTML = '<p style="text-align: center; color: #999;">No tickets added yet</p>';
            return;
        }
        
        tickets.forEach(ticket => {
            container.innerHTML += `
                <div class="list-item">
                    <div class="item-details">
                        <div class="item-field"><strong>Route:</strong> ${ticket.departure_terminal} → ${ticket.arrival_terminal}</div>
                        <div class="item-field"><strong>Passenger Age:</strong> ${ticket.age}</div>
                    </div>
                    <div class="item-actions">
                        <button class="btn-danger" onclick="deleteTicket(${ticket.id})">Delete</button>
                    </div>
                </div>
            `;
        });
    } catch (error) {
        showMessage('Error loading tickets', true);
    }
}

async function deleteTicket(id) {
    if (!confirm('Delete this ticket?')) return;
    try {
        const response = await fetch(`/api/tickets/${id}`, { method: 'DELETE' });
        if (response.ok) {
            showMessage('Ticket deleted successfully!');
            loadTickets();
        } else {
            showMessage('Error deleting ticket', true);
        }
    } catch (error) {
        showMessage('Error: ' + error.message, true);
    }
}

// Load initial data
window.addEventListener('load', () => {
    loadBuses();
});
