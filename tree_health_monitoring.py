from main import cursor, get_choice, get_input, conn, display_table, current_date


# Tree Health Monitoring
def tree_health_menu():
    options = ["1. Record Tree Health", "2. View Trees", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        record_tree_health()
    elif choice == "2":
        view_trees()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Try again.")


def record_tree_health():
    tree_id = get_input("Enter Tree ID")
    height = get_input("Enter Tree Height (in meters)")
    leaf_health = get_input("Enter Leaf Health (Good/Fair/Poor)")
    date = current_date()

    cursor.execute(
        """INSERT INTO trees (tree_id, height, leaf_health, date)
                      VALUES (?, ?, ?, ?)""",
        (tree_id, height, leaf_health, date),
    )
    conn.commit()

    print("Tree health recorded successfully.")


def view_trees():
    cursor.execute("SELECT tree_id, height, leaf_health, date FROM trees")
    rows = cursor.fetchall()

    if not rows:
        print("No trees recorded yet.")
    else:
        headers = ["Tree ID", "Height", "Leaf Health", "Date"]
        display_table(rows, headers)
