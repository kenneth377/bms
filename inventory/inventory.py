import json
import csv
from .item import Item

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return
        print("Item not found in inventory.")

    def update_item_quantity(self, item_name, new_quantity):
        for item in self.items:
            if item.name == item_name:
                item.update_quantity(new_quantity)
                return
        print("Item not found in inventory.")

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump([vars(item) for item in self.items], file)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.items = [Item(item['name'], item['price'], item['quantity']) for item in data]

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'price', 'quantity'])
            writer.writeheader()
            for item in self.items:
                writer.writerow(vars(item))

    def load_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            self.items = [Item(row['name'], float(row['price']), int(row['quantity'])) for row in reader]


# Learning is a journey