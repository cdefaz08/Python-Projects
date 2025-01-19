class Item:
    def __init__(self, item_code, price, stock):
        self.item_code = item_code
        self.price = price
        self.stock = int(stock)  # Convert stock to integer for proper arithmetic
        self.available = True

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"{quantity} items of {self.item_code} have been sold. {self.stock} remaining.")
        else:
            print(f"Not enough stock of {self.item_code} to sell.")

class Store:
    def __init__(self):
        self.items = []

    def add_item_code(self, item):
        self.items.append(item)
        print(f"Item code {item.item_code} has been added successfully. You have {item.stock} pcs on hand.")

    def remove_item_code(self, item):
        self.items.remove(item)
        print(f"Item code {item.item_code} has been removed successfully.")

    def sell(self, item_code, quantity):
        for item in self.items:
            if item.item_code == item_code:
                item.reduce_stock(quantity)
                break
        else:
            print(f"Item with code {item_code} not found in the store.")

# Create items
item1 = Item("papas", "5", "20")
item2 = Item("cocaola", "2", "10")

# Create store and add items
store = Store()
store.add_item_code(item1)
store.add_item_code(item2)

# Sell some items
store.sell("papas", 5)  # Reduce stock of "papas" by 5
store.sell("cocaola", 3)  # Reduce stock of "cocaola" by 3
store.sell("papas", 30)  # Trying to sell more than available stock

