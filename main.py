import sys
import sqlite3
from tabulate import tabulate
import datetime


# Connect to SQLite database
conn = sqlite3.connect("avocado_farm.db")
cursor = conn.cursor()


# Utility functions for input and date handling
def get_input(prompt):
    return input(f"{prompt}: ").strip()


def current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def display_table(data, headers):
    print(tabulate(data, headers, tablefmt="grid"))
    print("\n")


def main_menu():
    options = [
        "1. Tree Health Monitoring",
        "2. Irrigation Management",
        "3. Harvest Planning & Management",
        "4. Inventory Management",
        "5. Sales and Distribution Tracking",
        "6. Farm Expense Tracking",
        "7. Reports and Analytics",
        "8. Weather Data Integration",
        "9. Exit",
    ]
    print("\n".join(options))


def get_choice():
    return input(">> ")


# Main loop
def main():
    from initialize_db import initialize_db

    initialize_db()

    while True:
        main_menu()
        choice = get_choice()

        if choice == "1":
            from tree_health_monitoring import tree_health_menu

            tree_health_menu()
        elif choice == "2":
            from irrigation_management import irrigation_menu

            irrigation_menu()
        elif choice == "3":
            from harvest_menu import harvest_menu

            harvest_menu()
        elif choice == "4":
            from inventory_management import inventory_menu

            inventory_menu()
        elif choice == "5":
            print("Sales and Distribution feature coming soon!")
        elif choice == "6":
            from expense_menu import expense_menu

            expense_menu()
        elif choice == "7":
            print("Reports and Analytics feature coming soon!")
        elif choice == "8":
            from weather import view_weather_data

            view_weather_data()
        elif choice == "9":
            print("Goodbye!")
            conn.close()
            sys.exit()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
