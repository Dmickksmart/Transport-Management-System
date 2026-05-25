import sqlite3

def create_table():
    conn = sqlite3.connect("passengers.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS passengers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            gender TEXT,
            luggage_weight INTEGER)
        """
    )
    conn.commit()
    conn.close()

def add_passenger(first_name, last_name, age, gender, luggage_weight):
    conn = sqlite3.connect("passengers.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO passengers(first_name, last_name, age, gender, luggage_weight) VALUES (?, ?, ?, ?, ?)",
        (first_name, last_name, age, gender, luggage_weight),
    )
    conn.commit()
    conn.close()

def list_passengers():
    conn = sqlite3.connect("passengers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passengers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_passenger(passenger_id, first_name, last_name, age, gender, luggage_weight):
    conn = sqlite3.connect("passengers.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE passengers SET first_name = ?, last_name = ?, age = ?, gender = ?, luggage_weight = ? WHERE id = ?",
        (first_name, last_name, age, gender, luggage_weight, passenger_id),
    )
    conn.commit()
    conn.close()

def remove_passenger(passenger_id):
    conn = sqlite3.connect("passengers.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passengers WHERE id = ?", (passenger_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Passenger backend module initialized.")
