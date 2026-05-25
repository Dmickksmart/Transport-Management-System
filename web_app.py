from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database helper functions
def get_db_connection(db_name):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

def init_databases():
    """Initialize all databases"""
    # Bus
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bus(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT,
            brand TEXT,
            model TEXT,
            color TEXT,
            year INTEGER)
    """)
    conn.commit()
    conn.close()

    # Drivers
    conn = sqlite3.connect("drivers.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nin TEXT,
            first_name TEXT,
            last_name TEXT,
            driver_license TEXT,
            age INTEGER,
            gender TEXT)
    """)
    conn.commit()
    conn.close()

    # Passengers
    conn = sqlite3.connect("passengers.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passengers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            gender TEXT,
            luggage_weight INTEGER)
    """)
    conn.commit()
    conn.close()

    # Tickets
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            departure_terminal TEXT,
            arrival_terminal TEXT,
            age INTEGER)
    """)
    conn.commit()
    conn.close()

# ==================== ROUTES ====================

@app.route('/')
def index():
    return render_template('index.html')

# ==================== BUS ROUTES ====================

@app.route('/api/buses', methods=['GET', 'POST'])
def buses():
    if request.method == 'POST':
        data = request.json
        try:
            conn = get_db_connection("bus.db")
            conn.execute("INSERT INTO bus (plate_number, brand, model, color, year) VALUES (?, ?, ?, ?, ?)",
                        (data['plate_number'], data['brand'], data['model'], data['color'], int(data['year'])))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Bus added successfully'}), 201
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    conn = get_db_connection("bus.db")
    buses = conn.execute("SELECT * FROM bus").fetchall()
    conn.close()
    return jsonify([dict(bus) for bus in buses])

@app.route('/api/buses/<int:bus_id>', methods=['GET', 'PUT', 'DELETE'])
def bus_detail(bus_id):
    if request.method == 'GET':
        conn = get_db_connection("bus.db")
        bus = conn.execute("SELECT * FROM bus WHERE id = ?", (bus_id,)).fetchone()
        conn.close()
        return jsonify(dict(bus) if bus else {})

    if request.method == 'PUT':
        data = request.json
        try:
            conn = get_db_connection("bus.db")
            conn.execute("UPDATE bus SET plate_number = ?, brand = ?, model = ?, color = ?, year = ? WHERE id = ?",
                        (data['plate_number'], data['brand'], data['model'], data['color'], int(data['year']), bus_id))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Bus updated successfully'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    if request.method == 'DELETE':
        conn = get_db_connection("bus.db")
        conn.execute("DELETE FROM bus WHERE id = ?", (bus_id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Bus deleted successfully'})

# ==================== DRIVER ROUTES ====================

@app.route('/api/drivers', methods=['GET', 'POST'])
def drivers():
    if request.method == 'POST':
        data = request.json
        try:
            conn = get_db_connection("drivers.db")
            conn.execute("INSERT INTO drivers (nin, first_name, last_name, driver_license, age, gender) VALUES (?, ?, ?, ?, ?, ?)",
                        (data['nin'], data['first_name'], data['last_name'], data['driver_license'], int(data['age']), data['gender']))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Driver added successfully'}), 201
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    conn = get_db_connection("drivers.db")
    drivers_list = conn.execute("SELECT * FROM drivers").fetchall()
    conn.close()
    return jsonify([dict(driver) for driver in drivers_list])

@app.route('/api/drivers/<int:driver_id>', methods=['GET', 'PUT', 'DELETE'])
def driver_detail(driver_id):
    if request.method == 'GET':
        conn = get_db_connection("drivers.db")
        driver = conn.execute("SELECT * FROM drivers WHERE id = ?", (driver_id,)).fetchone()
        conn.close()
        return jsonify(dict(driver) if driver else {})

    if request.method == 'PUT':
        data = request.json
        try:
            conn = get_db_connection("drivers.db")
            conn.execute("UPDATE drivers SET nin = ?, first_name = ?, last_name = ?, driver_license = ?, age = ?, gender = ? WHERE id = ?",
                        (data['nin'], data['first_name'], data['last_name'], data['driver_license'], int(data['age']), data['gender'], driver_id))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Driver updated successfully'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    if request.method == 'DELETE':
        conn = get_db_connection("drivers.db")
        conn.execute("DELETE FROM drivers WHERE id = ?", (driver_id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Driver deleted successfully'})

# ==================== PASSENGER ROUTES ====================

@app.route('/api/passengers', methods=['GET', 'POST'])
def passengers():
    if request.method == 'POST':
        data = request.json
        try:
            conn = get_db_connection("passengers.db")
            conn.execute("INSERT INTO passengers (first_name, last_name, age, gender, luggage_weight) VALUES (?, ?, ?, ?, ?)",
                        (data['first_name'], data['last_name'], int(data['age']), data['gender'], int(data['luggage_weight'])))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Passenger added successfully'}), 201
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    conn = get_db_connection("passengers.db")
    passengers_list = conn.execute("SELECT * FROM passengers").fetchall()
    conn.close()
    return jsonify([dict(passenger) for passenger in passengers_list])

@app.route('/api/passengers/<int:passenger_id>', methods=['GET', 'PUT', 'DELETE'])
def passenger_detail(passenger_id):
    if request.method == 'GET':
        conn = get_db_connection("passengers.db")
        passenger = conn.execute("SELECT * FROM passengers WHERE id = ?", (passenger_id,)).fetchone()
        conn.close()
        return jsonify(dict(passenger) if passenger else {})

    if request.method == 'PUT':
        data = request.json
        try:
            conn = get_db_connection("passengers.db")
            conn.execute("UPDATE passengers SET first_name = ?, last_name = ?, age = ?, gender = ?, luggage_weight = ? WHERE id = ?",
                        (data['first_name'], data['last_name'], int(data['age']), data['gender'], int(data['luggage_weight']), passenger_id))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Passenger updated successfully'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    if request.method == 'DELETE':
        conn = get_db_connection("passengers.db")
        conn.execute("DELETE FROM passengers WHERE id = ?", (passenger_id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Passenger deleted successfully'})

# ==================== TICKET ROUTES ====================

@app.route('/api/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        data = request.json
        try:
            conn = get_db_connection("tickets.db")
            conn.execute("INSERT INTO tickets (departure_terminal, arrival_terminal, age) VALUES (?, ?, ?)",
                        (data['departure_terminal'], data['arrival_terminal'], int(data['age'])))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Ticket added successfully'}), 201
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    conn = get_db_connection("tickets.db")
    tickets_list = conn.execute("SELECT * FROM tickets").fetchall()
    conn.close()
    return jsonify([dict(ticket) for ticket in tickets_list])

@app.route('/api/tickets/<int:ticket_id>', methods=['GET', 'PUT', 'DELETE'])
def ticket_detail(ticket_id):
    if request.method == 'GET':
        conn = get_db_connection("tickets.db")
        ticket = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
        conn.close()
        return jsonify(dict(ticket) if ticket else {})

    if request.method == 'PUT':
        data = request.json
        try:
            conn = get_db_connection("tickets.db")
            conn.execute("UPDATE tickets SET departure_terminal = ?, arrival_terminal = ?, age = ? WHERE id = ?",
                        (data['departure_terminal'], data['arrival_terminal'], int(data['age']), ticket_id))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Ticket updated successfully'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

    if request.method == 'DELETE':
        conn = get_db_connection("tickets.db")
        conn.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Ticket deleted successfully'})

if __name__ == '__main__':
    init_databases()
    app.run(debug=True, host='0.0.0.0', port=5000)
