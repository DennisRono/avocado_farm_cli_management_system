from main import cursor, get_choice, get_input, conn, display_table, current_date


# Expense Tracking
def expense_menu():
    options = ["1. Log Expense", "2. View Expenses", "3. Go Back"]
    print("\n".join(options))
    choice = get_choice()

    if choice == "1":
        log_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Try again.")


def log_expense():
    category = get_input("Enter Expense Category")
    amount = get_input("Enter Amount")
    description = get_input("Enter Description")
    date = current_date()

    cursor.execute(
        """INSERT INTO expenses (category, amount, description, date)
                      VALUES (?, ?, ?, ?)""",
        (category, amount, description, date),
    )
    conn.commit()

    print("Expense logged.")


def view_expenses():
    cursor.execute("SELECT category, amount, description, date FROM expenses")
    rows = cursor.fetchall()

    if not rows:
        print("No expense records.")
    else:
        headers = ["Category", "Amount", "Description", "Date"]
        display_table(rows, headers)
