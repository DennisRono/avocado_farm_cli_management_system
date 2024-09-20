from colorama import Fore
from InquirerPy import prompt
import colorama
from datetime import datetime
from initialize_db import Distribution, Sale
from main import display_table, loading_simulation, session

colorama.init(autoreset=True)


def add_sale():
    questions = [
        {"type": "input", "message": "Enter buyer's name:", "name": "buyer_name"},
        {
            "type": "input",
            "message": "Enter quantity sold (kg):",
            "name": "quantity",
            "validate": lambda val: val.isdigit() or "Please enter a valid number",
            "filter": lambda val: float(val),
        },
        {
            "type": "input",
            "message": "Enter price per kg:",
            "name": "price",
            "validate": lambda val: val.replace(".", "", 1).isdigit()
            or "Please enter a valid number",
            "filter": lambda val: float(val),
        },
        {"type": "input", "message": "Enter sale date (YYYY-MM-DD):", "name": "date"},
    ]

    answers = prompt(questions)
    buyer_name = answers["buyer_name"]
    quantity = answers["quantity"]
    price = float(answers["price"])

    # Convert the date string to a datetime.date object
    try:
        sale_date = datetime.strptime(answers["date"], "%Y-%m-%d").date()
    except ValueError:
        print(
            Fore.RED
            + "Invalid date format. Please enter the date in YYYY-MM-DD format."
        )
        return

    loading_simulation("Adding sale")

    try:
        sale = Sale(
            buyer_name=buyer_name, quantity=quantity, price=price, date=sale_date
        )
        session.add(sale)
        session.commit()
        print(Fore.GREEN + "Sale added successfully.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        session.rollback()


def view_sales():
    sales = session.query(Sale).all()
    if not sales:
        print(Fore.YELLOW + "No sales recorded yet.")
    else:
        print(Fore.CYAN + "Sales Records:")
        headers = ["ID", "Buyer Name", "Quantity", "Price", "Date"]
        rows = [
            (sale.id, sale.buyer_name, sale.quantity, sale.price, sale.date)
            for sale in sales
        ]
        display_table(rows, headers)


def add_distribution():
    questions = [
        {
            "type": "input",
            "message": "Enter distributor's name:",
            "name": "distributor_name",
        },
        {
            "type": "input",
            "message": "Enter quantity distributed (kg):",
            "name": "quantity",
            "validate": lambda val: val.isdigit() or "Please enter a valid number",
            "filter": lambda val: float(val),
        },
        {
            "type": "input",
            "message": "Enter distribution date (YYYY-MM-DD):",
            "name": "date",
        },
    ]

    answers = prompt(questions)
    distributor_name = answers["distributor_name"]
    quantity = answers["quantity"]

    # Convert the date string to a datetime.date object
    try:
        distribution_date = datetime.strptime(answers["date"], "%Y-%m-%d").date()
    except ValueError:
        print(
            Fore.RED
            + "Invalid date format. Please enter the date in YYYY-MM-DD format."
        )
        return

    loading_simulation("Adding distribution")

    try:
        distribution = Distribution(
            distributor_name=distributor_name, quantity=quantity, date=distribution_date
        )
        session.add(distribution)
        session.commit()
        print(Fore.GREEN + "Distribution added successfully.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        session.rollback()


def view_distribution():
    distribution = session.query(Distribution).all()
    if not distribution:
        print(Fore.YELLOW + "No distribution records yet.")
    else:
        print(Fore.CYAN + "Distribution Records:")
        headers = ["ID", "Distributor Name", "Quantity", "Date"]
        rows = [
            (dist.id, dist.distributor_name, dist.quantity, dist.date)
            for dist in distribution
        ]
        display_table(rows, headers)


def sales_management():
    while True:
        menu_question = {
            "type": "list",
            "message": "Choose an option:",
            "choices": [
                "Add Sale",
                "View Sales",
                "Add Distribution",
                "View Distribution",
                "Exit",
            ],
            "name": "option",
        }
        answer = prompt(menu_question)

        if answer["option"] == "Add Sale":
            add_sale()
        elif answer["option"] == "View Sales":
            view_sales()
        elif answer["option"] == "Add Distribution":
            add_distribution()
        elif answer["option"] == "View Distribution":
            view_distribution()
        elif answer["option"] == "Exit":
            break
