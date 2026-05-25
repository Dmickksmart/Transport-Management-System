import sqlite3
import customtkinter as ctk
from tkinter import messagebox


def create_table():
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS bus(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT,
            brand TEXT,
            model TEXT,
            color TEXT,
            year INTEGER)
        """
    )
    conn.commit()
    conn.close()


def add_bus(plate_number, brand, model, color, year):
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bus(plate_number, brand, model, color, year) VALUES (?, ?, ?, ?, ?)",
        (plate_number, brand, model, color, year),
    )
    conn.commit()
    conn.close()


def update_bus(bus_id, plate_number, brand, model, color, year):
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE bus SET plate_number = ?, brand = ?, model = ?, color = ?, year = ? WHERE id = ?",
        (plate_number, brand, model, color, year, bus_id),
    )
    conn.commit()
    conn.close()


def remove_bus(bus_id):
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bus WHERE id = ?", (bus_id,))
    conn.commit()
    conn.close()


def list_bus():
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bus")
    buses = cursor.fetchall()
    conn.close()
    return buses


if __name__ == "__main__":
    create_table()
    root = ctk.CTk()
    root.title("Bus Management App")
    root.geometry("800x600")

    fields = [
        ("Plate Number", "plate_number"),
        ("Brand", "brand"),
        ("Model", "model"),
        ("Color", "color"),
        ("Year", "year"),
    ]

    entries = {}
    for label_text, field_name in fields:
        label = ctk.CTkLabel(root, text=label_text)
        label.pack()
        entry = ctk.CTkEntry(root)
        entry.pack()
        entries[field_name] = entry

    def add_bus_command():
        try:
            year_value = int(entries["year"].get().strip())
        except ValueError:
            messagebox.showerror("Validation Error", "Year must be an integer.")
            return
        add_bus(
            entries["plate_number"].get().strip(),
            entries["brand"].get().strip(),
            entries["model"].get().strip(),
            entries["color"].get().strip(),
            year_value,
        )
        messagebox.showinfo("Success", "Bus details have been added.")

    add_button = ctk.CTkButton(root, text="Add Bus", command=add_bus_command)
    add_button.pack()

    def list_bus_command():
        buses = list_bus()
        text_window = ctk.CTkToplevel(root)
        text_window.title("Bus List")
        text_box = ctk.CTkTextbox(text_window, width=500, height=300)
        text_box.pack(fill="both", expand=True)
        if not buses:
            text_box.insert("0.0", "No buses found.\n")
        else:
            for bus in buses:
                text_box.insert("0.0", f"{bus}\n")

    list_button = ctk.CTkButton(root, text="List Bus", command=list_bus_command)
    list_button.pack()

    root.mainloop()
