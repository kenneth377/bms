from inventory.inventory import Inventory, Item

def main():
    inventory = Inventory()

    inventory.add_item(Item("Laptop", 1000, 5))
    inventory.add_item(Item("Mouse", 20, 10))
    inventory.add_item(Item("Keyboard", 50, 8))


    inventory.save_to_json("data/inventory.json")
    inventory.save_to_csv("data/inventory.csv")

    inventory.load_from_json("data/inventory.json")
    inventory.load_from_csv("data/inventory.csv")

    inventory.update_item_quantity("Mouse", 15)

    inventory.remove_item("Keyboard")

if __name__ == "__main__":
    main()
