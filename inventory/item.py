class Item:
    def __init__(self, *args, **kwargs):
        if args:
            try:
                if len(args) >= 1:
                    self.name = str(args[0])
                if len(args) >= 2:
                    self.price = float(args[1])
                if len(args) >= 3:
                    self.quantity = int(args[2])
            except ValueError as e:
                print(f"{e.__class__} : Names must be of type str, price of type float and quantity of type int")
        else:
            for key, value in kwargs.items():
                try:
                    if key == 'name':
                        self.name = str(value)
                    elif key == 'price':
                        self.price= float(value)
                    elif key == 'quantity':
                        self.quantity = int(value)
                except ValueError as e:
                    print(f"{e.__class__} : Names must be of type str, price of type float and quantity of type int")

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
