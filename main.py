import sqlite3
import customtkinter as ctk
from tkinter import ttk, messagebox


def create_table_bus():
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
        """
    )
    conn.commit()
    conn.close()


def create_table_drivers():
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


def create_table_passengers():
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


def create_table_tickets():
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


def parse_int(value, name):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"{name} must be a number")


def add_bus(plate, brand, model, color, year):
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bus(plate_number, brand, model, color, year) VALUES (?, ?, ?, ?, ?)",
        (plate, brand, model, color, year),
    )
    conn.commit()
    conn.close()


def list_bus():
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bus")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_bus(bus_id, plate, brand, model, color, year):
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE bus SET plate_number = ?, brand = ?, model = ?, color = ?, year = ? WHERE id = ?",
        (plate, brand, model, color, year, bus_id),
    )
    conn.commit()
    conn.close()


def remove_bus(bus_id):
    conn = sqlite3.connect("bus.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bus WHERE id = ?", (bus_id,))
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


def create_form_inputs(parent, fields, start_row=0):
    entries = {}
    for index, (label_text, field_name) in enumerate(fields):
        label = ctk.CTkLabel(parent, text=label_text)
        label.grid(row=start_row + index, column=0, padx=8, pady=6, sticky="w")
        entry = ctk.CTkEntry(parent)
        entry.grid(row=start_row + index, column=1, padx=8, pady=6, sticky="ew")
        entries[field_name] = entry
    return entries


def clear_entries(entries):
    for entry in entries.values():
        entry.delete(0, "end")


def display_rows(tree, rows):
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", "end", values=row)


def build_bus_tab(parent):
    fields = [
        ("ID (for update/remove)", "id"),
        ("Plate Number", "plate_number"),
        ("Brand", "brand"),
        ("Model", "model"),
        ("Color", "color"),
        ("Year", "year"),
    ]
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True, padx=12, pady=12)
    entries = create_form_inputs(frame, fields)
    frame.columnconfigure(1, weight=1)

    button_frame = ctk.CTkFrame(frame)
    button_frame.grid(row=len(fields), column=0, columnspan=2, pady=10, sticky="w")
    bus_tree = ttk.Treeview(frame, columns=("id", "plate_number", "brand", "model", "color", "year"), show="headings", height=10)
    for col, heading in [
        ("id", "ID"),
        ("plate_number", "Plate"),
        ("brand", "Brand"),
        ("model", "Model"),
        ("color", "Color"),
        ("year", "Year"),
    ]:
        bus_tree.heading(col, text=heading)
        bus_tree.column(col, width=100, anchor="center")
    bus_tree.grid(row=0, column=2, rowspan=len(fields) + 1, padx=12, pady=4, sticky="nsew")
    frame.columnconfigure(2, weight=1)

    def bus_add_action():
        try:
            year_value = parse_int(entries["year"].get().strip(), "Year")
            add_bus(
                entries["plate_number"].get().strip(),
                entries["brand"].get().strip(),
                entries["model"].get().strip(),
                entries["color"].get().strip(),
                year_value,
            )
            messagebox.showinfo("Success", "Bus details have been added.")
            clear_entries(entries)
            display_rows(bus_tree, list_bus())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def bus_update_action():
        try:
            bus_id = parse_int(entries["id"].get().strip(), "Bus ID")
            year_value = parse_int(entries["year"].get().strip(), "Year")
            update_bus(
                bus_id,
                entries["plate_number"].get().strip(),
                entries["brand"].get().strip(),
                entries["model"].get().strip(),
                entries["color"].get().strip(),
                year_value,
            )
            messagebox.showinfo("Success", "Bus details have been updated.")
            clear_entries(entries)
            display_rows(bus_tree, list_bus())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def bus_remove_action():
        try:
            bus_id = parse_int(entries["id"].get().strip(), "Bus ID")
            remove_bus(bus_id)
            messagebox.showinfo("Success", "Bus record has been removed.")
            clear_entries(entries)
            display_rows(bus_tree, list_bus())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def bus_list_action():
        display_rows(bus_tree, list_bus())

    ctk.CTkButton(button_frame, text="Add Bus", command=bus_add_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="Update Bus", command=bus_update_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="Remove Bus", command=bus_remove_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="List Buses", command=bus_list_action).pack(side="left", padx=6)

    bus_list_action()
    return frame


def build_driver_tab(parent):
    fields = [
        ("ID (for update/remove)", "id"),
        ("NIN", "nin"),
        ("First Name", "first_name"),
        ("Last Name", "last_name"),
        ("Driver License", "driver_license"),
        ("Age", "age"),
        ("Gender", "gender"),
    ]
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True, padx=12, pady=12)
    entries = create_form_inputs(frame, fields)
    frame.columnconfigure(1, weight=1)

    button_frame = ctk.CTkFrame(frame)
    button_frame.grid(row=len(fields), column=0, columnspan=2, pady=10, sticky="w")
    driver_tree = ttk.Treeview(frame, columns=("id", "nin", "first_name", "last_name", "driver_license", "age", "gender"), show="headings", height=10)
    for col, heading in [
        ("id", "ID"),
        ("nin", "NIN"),
        ("first_name", "First"),
        ("last_name", "Last"),
        ("driver_license", "License"),
        ("age", "Age"),
        ("gender", "Gender"),
    ]:
        driver_tree.heading(col, text=heading)
        driver_tree.column(col, width=100, anchor="center")
    driver_tree.grid(row=0, column=2, rowspan=len(fields) + 1, padx=12, pady=4, sticky="nsew")
    frame.columnconfigure(2, weight=1)

    def driver_add_action():
        try:
            age_value = parse_int(entries["age"].get().strip(), "Age")
            add_driver(
                entries["nin"].get().strip(),
                entries["first_name"].get().strip(),
                entries["last_name"].get().strip(),
                entries["driver_license"].get().strip(),
                age_value,
                entries["gender"].get().strip(),
            )
            messagebox.showinfo("Success", "Driver details have been added.")
            clear_entries(entries)
            display_rows(driver_tree, list_drivers())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def driver_update_action():
        try:
            driver_id = parse_int(entries["id"].get().strip(), "Driver ID")
            age_value = parse_int(entries["age"].get().strip(), "Age")
            update_driver(
                driver_id,
                entries["nin"].get().strip(),
                entries["first_name"].get().strip(),
                entries["last_name"].get().strip(),
                entries["driver_license"].get().strip(),
                age_value,
                entries["gender"].get().strip(),
            )
            messagebox.showinfo("Success", "Driver details have been updated.")
            clear_entries(entries)
            display_rows(driver_tree, list_drivers())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def driver_remove_action():
        try:
            driver_id = parse_int(entries["id"].get().strip(), "Driver ID")
            remove_driver(driver_id)
            messagebox.showinfo("Success", "Driver record has been removed.")
            clear_entries(entries)
            display_rows(driver_tree, list_drivers())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def driver_list_action():
        display_rows(driver_tree, list_drivers())

    ctk.CTkButton(button_frame, text="Add Driver", command=driver_add_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="Update Driver", command=driver_update_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="Remove Driver", command=driver_remove_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="List Drivers", command=driver_list_action).pack(side="left", padx=6)

    driver_list_action()
    return frame


def build_passenger_tab(parent):
    fields = [
        ("ID (for update/remove)", "id"),
        ("First Name", "first_name"),
        ("Last Name", "last_name"),
        ("Age", "age"),
        ("Gender", "gender"),
        ("Luggage Weight", "luggage_weight"),
    ]
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True, padx=12, pady=12)
    entries = create_form_inputs(frame, fields)
    frame.columnconfigure(1, weight=1)

    button_frame = ctk.CTkFrame(frame)
    button_frame.grid(row=len(fields), column=0, columnspan=2, pady=10, sticky="w")
    passenger_tree = ttk.Treeview(frame, columns=("id", "first_name", "last_name", "age", "gender", "luggage_weight"), show="headings", height=10)
    for col, heading in [
        ("id", "ID"),
        ("first_name", "First"),
        ("last_name", "Last"),
        ("age", "Age"),
        ("gender", "Gender"),
        ("luggage_weight", "Luggage"),
    ]:
        passenger_tree.heading(col, text=heading)
        passenger_tree.column(col, width=100, anchor="center")
    passenger_tree.grid(row=0, column=2, rowspan=len(fields) + 1, padx=12, pady=4, sticky="nsew")
    frame.columnconfigure(2, weight=1)

    def passenger_add_action():
        try:
            age_value = parse_int(entries["age"].get().strip(), "Age")
            luggage_value = parse_int(entries["luggage_weight"].get().strip(), "Luggage Weight")
            add_passenger(
                entries["first_name"].get().strip(),
                entries["last_name"].get().strip(),
                age_value,
                entries["gender"].get().strip(),
                luggage_value,
            )
            messagebox.showinfo("Success", "Passenger details have been added.")
            clear_entries(entries)
            display_rows(passenger_tree, list_passengers())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def passenger_update_action():
        try:
            passenger_id = parse_int(entries["id"].get().strip(), "Passenger ID")
            age_value = parse_int(entries["age"].get().strip(), "Age")
            luggage_value = parse_int(entries["luggage_weight"].get().strip(), "Luggage Weight")
            update_passenger(
                passenger_id,
                entries["first_name"].get().strip(),
                entries["last_name"].get().strip(),
                age_value,
                entries["gender"].get().strip(),
                luggage_value,
            )
            messagebox.showinfo("Success", "Passenger details have been updated.")
            clear_entries(entries)
            display_rows(passenger_tree, list_passengers())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def passenger_remove_action():
        try:
            passenger_id = parse_int(entries["id"].get().strip(), "Passenger ID")
            remove_passenger(passenger_id)
            messagebox.showinfo("Success", "Passenger record has been removed.")
            clear_entries(entries)
            display_rows(passenger_tree, list_passengers())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def passenger_list_action():
        display_rows(passenger_tree, list_passengers())

    ctk.CTkButton(button_frame, text="Add Passenger", command=passenger_add_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="Update Passenger", command=passenger_update_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="Remove Passenger", command=passenger_remove_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="List Passengers", command=passenger_list_action).pack(side="left", padx=6)

    passenger_list_action()
    return frame


def build_ticket_tab(parent):
    fields = [
        ("ID (for update/remove)", "id"),
        ("Departure Terminal", "departure_terminal"),
        ("Arrival Terminal", "arrival_terminal"),
        ("Age", "age"),
    ]
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True, padx=12, pady=12)
    entries = create_form_inputs(frame, fields)
    frame.columnconfigure(1, weight=1)

    button_frame = ctk.CTkFrame(frame)
    button_frame.grid(row=len(fields), column=0, columnspan=2, pady=10, sticky="w")
    ticket_tree = ttk.Treeview(frame, columns=("id", "departure_terminal", "arrival_terminal", "age"), show="headings", height=10)
    for col, heading in [
        ("id", "ID"),
        ("departure_terminal", "Departure"),
        ("arrival_terminal", "Arrival"),
        ("age", "Age"),
    ]:
        ticket_tree.heading(col, text=heading)
        ticket_tree.column(col, width=130, anchor="center")
    ticket_tree.grid(row=0, column=2, rowspan=len(fields) + 1, padx=12, pady=4, sticky="nsew")
    frame.columnconfigure(2, weight=1)

    def ticket_add_action():
        try:
            age_value = parse_int(entries["age"].get().strip(), "Age")
            add_ticket(
                entries["departure_terminal"].get().strip(),
                entries["arrival_terminal"].get().strip(),
                age_value,
            )
            messagebox.showinfo("Success", "Ticket details have been added.")
            clear_entries(entries)
            display_rows(ticket_tree, list_tickets())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def ticket_update_action():
        try:
            ticket_id = parse_int(entries["id"].get().strip(), "Ticket ID")
            age_value = parse_int(entries["age"].get().strip(), "Age")
            update_ticket(
                ticket_id,
                entries["departure_terminal"].get().strip(),
                entries["arrival_terminal"].get().strip(),
                age_value,
            )
            messagebox.showinfo("Success", "Ticket details have been updated.")
            clear_entries(entries)
            display_rows(ticket_tree, list_tickets())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def ticket_remove_action():
        try:
            ticket_id = parse_int(entries["id"].get().strip(), "Ticket ID")
            remove_ticket(ticket_id)
            messagebox.showinfo("Success", "Ticket record has been removed.")
            clear_entries(entries)
            display_rows(ticket_tree, list_tickets())
        except ValueError as error:
            messagebox.showerror("Validation Error", str(error))

    def ticket_list_action():
        display_rows(ticket_tree, list_tickets())

    ctk.CTkButton(button_frame, text="Add Ticket", command=ticket_add_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="Update Ticket", command=ticket_update_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="Remove Ticket", command=ticket_remove_action).pack(side="left", padx=6)
    ctk.CTkButton(button_frame, text="List Tickets", command=ticket_list_action).pack(side="left", padx=6)

    ticket_list_action()
    return frame


def main():
    create_table_bus()
    create_table_drivers()
    create_table_passengers()
    create_table_tickets()

    root = ctk.CTk()
    root.title("Transport Management System")
    root.geometry("1080x650")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    bus_tab = ctk.CTkFrame(notebook)
    driver_tab = ctk.CTkFrame(notebook)
    passenger_tab = ctk.CTkFrame(notebook)
    ticket_tab = ctk.CTkFrame(notebook)

    notebook.add(bus_tab, text="Bus")
    notebook.add(driver_tab, text="Drivers")
    notebook.add(passenger_tab, text="Passengers")
    notebook.add(ticket_tab, text="Tickets")

    build_bus_tab(bus_tab)
    build_driver_tab(driver_tab)
    build_passenger_tab(passenger_tab)
    build_ticket_tab(ticket_tab)

    root.mainloop()


if __name__ == "__main__":
    main()
