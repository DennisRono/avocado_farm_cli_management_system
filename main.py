import sys
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from colorama import init, Fore, Style
from tqdm import tqdm
import time

init(autoreset=True)

engine = create_engine("sqlite:///avocado_farm.db")
Session = sessionmaker(bind=engine)
session = Session()


def get_input(prompt):
    return input(f"{Fore.CYAN}{prompt}: {Style.RESET_ALL}").strip()


def current_date():
    return datetime.datetime.now()


def display_table(data, headers):
    print(Fore.GREEN + tabulate(data, headers, tablefmt="grid"))
    print("\n")


def loading_simulation(text):
    for _ in tqdm(range(50), desc=text, ncols=75, ascii=True):
        time.sleep(0.01)


def main_menu():
    options = [
        f"{Fore.YELLOW}1. Manage Trees (Add and Varieties)",
        f"{Fore.YELLOW}2. Tree Health Monitoring",
        f"{Fore.YELLOW}3. Irrigation Management",
        f"{Fore.YELLOW}4. Harvest Planning & Management",
        f"{Fore.YELLOW}5. Inventory Management",
        f"{Fore.YELLOW}6. Sales and Distribution Tracking",
        f"{Fore.YELLOW}7. Farm Expense Tracking",
        f"{Fore.YELLOW}8. Reports and Analytics",
        f"{Fore.YELLOW}9. Weather Data Integration",
        f"{Fore.RED}10. Exit{Style.RESET_ALL}",
    ]
    print("\n".join(options))


def get_choice():
    return input(Fore.MAGENTA + ">> " + Style.RESET_ALL)


def main():
    from initialize_db import initialize_db

    initialize_db()

    while True:
        main_menu()
        choice = get_choice()

        if choice == "1":
            from add_tree import new_tree_opts

            new_tree_opts()
        elif choice == "2":
            from tree_health_monitoring import tree_health_menu

            tree_health_menu()
        elif choice == "3":
            from irrigation_management import irrigation_menu

            irrigation_menu()
        elif choice == "4":
            from harvest_menu import harvest_menu

            harvest_menu()
        elif choice == "5":
            from inventory_management import inventory_menu

            inventory_menu()
        elif choice == "6":
            from sales import sales_management

            sales_management()
        elif choice == "7":
            from expense_menu import expense_menu

            expense_menu()
        elif choice == "8":
            from reports import reports_menu

            reports_menu()
        elif choice == "9":
            from weather import view_weather_data

            view_weather_data()
        elif choice == "10":
            print(Fore.RED + "Goodbye!")
            session.close()
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice. Try again.")


if __name__ == "__main__":
    print(Fore.GREEN + "Welcome to Avocado Farm Management System!")
    main()
