from main import cursor, get_choice, get_input, conn, display_table, current_date


# Harvest Planning & Management
def harvest_menu():
    options = ["1. Log Harvest", "2. View Harvest Records", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_harvest()
    elif choice == "2":
        view_harvest_records()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Try again.")


def log_harvest():
    tree_id = get_input("Enter Tree ID")
    quantity = get_input("Enter Quantity Harvested (kg)")
    date = current_date()

    cursor.execute(
        """INSERT INTO harvest (tree_id, quantity, date)
                      VALUES (?, ?, ?)""",
        (tree_id, quantity, date),
    )
    conn.commit()

    print("Harvest logged.")


def view_harvest_records():
    cursor.execute("SELECT tree_id, quantity, date FROM harvest")
    rows = cursor.fetchall()

    if not rows:
        print("No harvest records.")
    else:
        headers = ["Tree ID", "Quantity", "Date"]
        display_table(rows, headers)
