import cmd
from inventory import inventory
from inventory import item

class Console(cmd.Cmd):
    def __init__(self) -> None:
        super().__init__()
        self.inventorne = inventory.Inventory()
        self.prompt =  ">>>>"

    def do_add(self, value):
        values = value.split(" ")
        self.inventorne.add_item(item.Item(values[0],values[1],values[2]))
        print(self.inventorne.items)
        self.inventorne.save_to_json("data/inventory.json")
        self.inventorne.save_to_csv("data/inventory.csv")

    def do_remove(self,value):
        for item in self.inventorne.items:
            if item.name == value:
                self.inventorne.items.remove(item)
                self.inventorne.save_to_json("data/inventory.json")
                self.inventorne.save_to_csv("data/inventory.csv")
                return
        print("Item not found")

    def do_update(self,value):
        values = value.split(" ")
        for item in self.inventorne.items:
            if item.name == values[0]:
                item.quantity = int(values[1])
                self.inventorne.save_to_json("data/inventory.json")
                self.inventorne.save_to_csv("data/inventory.csv")
                return
        print("Item does not exist")


    def do_quit(self):
        return True



if __name__ == "__main__":
    Console().cmdloop()