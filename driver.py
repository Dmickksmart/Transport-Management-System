import sqlite3
import customtkinter as ctk
from tkinter import messagebox


def create_table():
    conn = sqlite3.connect("drivers.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS drivers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nin TEXT,
            first_name TEXT,
            last_name TEXT,
            driver_license TEXT,
            age INTEGER,
            gender TEXT)
        """
    )
    conn.commit()
    conn.close()


def add_driver(nin, first_name, last_name, driver_license, age, gender):
    conn = sqlite3.connect("drivers.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO drivers(nin, first_name, last_name, driver_license, age, gender) VALUES (?, ?, ?, ?, ?, ?)",
        (nin, first_name, last_name, driver_license, age, gender),
    )
    conn.commit()
    conn.close()


def list_drivers():
    conn = sqlite3.connect("drivers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM drivers")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_driver(driver_id, nin, first_name, last_name, driver_license, age, gender):
    conn = sqlite3.connect("drivers.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE drivers SET nin = ?, first_name = ?, last_name = ?, driver_license = ?, age = ?, gender = ? WHERE id = ?",
        (nin, first_name, last_name, driver_license, age, gender, driver_id),
    )
    conn.commit()
    conn.close()


def remove_driver(driver_id):
    conn = sqlite3.connect("drivers.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM drivers WHERE id = ?", (driver_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    root = ctk.CTk()
    root.title("Driver Management App")
    root.geometry("650x450")

    labels = [
        "NIN",
        "First Name",
        "Last Name",
        "Driver License",
        "Age",
        "Gender",
    ]
    entries = {}
    for index, label_text in enumerate(labels):
        label = ctk.CTkLabel(root, text=label_text)
        label.grid(row=index, column=0, padx=10, pady=8, sticky="w")
        entry = ctk.CTkEntry(root)
        entry.grid(row=index, column=1, padx=10, pady=8, sticky="ew")
        entries[label_text.lower().replace(" ", "_")] = entry

    def add_driver_command():
        try:
            age_value = int(entries["age"].get().strip())
        except ValueError:
            messagebox.showerror("Validation Error", "Age must be an integer.")
            return

        add_driver(
            entries["nin"].get().strip(),
            entries["first_name"].get().strip(),
            entries["last_name"].get().strip(),
            entries["driver_license"].get().strip(),
            age_value,
            entries["gender"].get().strip(),
        )
        messagebox.showinfo("Success", "Driver details have been added.")

    add_button = ctk.CTkButton(root, text="Add Driver", command=add_driver_command)
    add_button.grid(row=len(labels), column=0, columnspan=2, pady=12)

    root.columnconfigure(1, weight=1)
    root.mainloop()
