from main import cursor, get_choice, get_input, conn, display_table, current_date


# Inventory Management
def inventory_menu():
    options = ["1. Log Inventory", "2. View Inventory", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_inventory()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Try again.")


def log_inventory():
    quantity = get_input("Enter Quantity (kg)")
    size = get_input("Enter Size (small/medium/large)")
    quality = get_input("Enter Quality (Good/Fair/Poor)")
    date = current_date()

    cursor.execute(
        """INSERT INTO inventory (quantity, size, quality, date)
                      VALUES (?, ?, ?, ?)""",
        (quantity, size, quality, date),
    )
    conn.commit()

    print("Inventory logged.")


def view_inventory():
    cursor.execute("SELECT quantity, size, quality, date FROM inventory")
    rows = cursor.fetchall()

    if not rows:
        print("No inventory records.")
    else:
        headers = ["Quantity", "Size", "Quality", "Date"]
        display_table(rows, headers)
