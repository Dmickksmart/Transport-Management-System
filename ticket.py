import sqlite3


def create_table():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tickets(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            departure_terminal TEXT,
            arrival_terminal TEXT,
            age INTEGER)
        """
    )
    conn.commit()
    conn.close()


def add_ticket(departure_terminal, arrival_terminal, age):
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tickets(departure_terminal, arrival_terminal, age) VALUES (?, ?, ?)",
        (departure_terminal, arrival_terminal, age),
    )
    conn.commit()
    conn.close()


def list_tickets():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_ticket(ticket_id, departure_terminal, arrival_terminal, age):
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tickets SET departure_terminal = ?, arrival_terminal = ?, age = ? WHERE id = ?",
        (departure_terminal, arrival_terminal, age, ticket_id),
    )
    conn.commit()
    conn.close()


def remove_ticket(ticket_id):
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Ticket backend module initialized.")
