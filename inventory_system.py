import json
from datetime import datetime
import ast

# Global variable for storing inventory
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a new item and its quantity to the stock data."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types. Item must be a string and quantity an integer.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove quantity of an item. If quantity <= 0, delete the item."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
        else:
            print(f"Item '{item}' not found in inventory.")
    except Exception as e:
        print(f"Error while removing item: {e}")


def get_qty(item):
    """Return quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """Save current stock data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Display all inventory items."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items with quantity below threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main program for testing inventory functions."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("grape", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    # Removed insecure eval() function


if __name__ == "__main__":
    main()
