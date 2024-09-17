from main import get_input, get_choice, cursor, conn, current_date, display_table


# Irrigation Management
def irrigation_menu():
    options = ["1. Log Irrigation Activity", "2. View Irrigation Records", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_irrigation_activity()
    elif choice == "2":
        view_irrigation_records()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Try again.")


def log_irrigation_activity():
    tree_id = get_input("Enter Tree ID")
    volume = get_input("Enter Water Volume (liters)")
    duration = get_input("Enter Duration (minutes)")
    date = current_date()

    cursor.execute(
        """INSERT INTO irrigation (tree_id, volume, duration, date)
                      VALUES (?, ?, ?, ?)""",
        (tree_id, volume, duration, date),
    )
    conn.commit()

    print("Irrigation activity logged.")


def view_irrigation_records():
    cursor.execute("SELECT tree_id, volume, duration, date FROM irrigation")
    rows = cursor.fetchall()

    if not rows:
        print("No irrigation records.")
    else:
        headers = ["Tree ID", "Volume", "Duration", "Date"]
        display_table(rows, headers)
