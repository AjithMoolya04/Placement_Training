#wrie a program to create a clsaa representing shoping cart,this includes methods for adding and removing items and calculating total price
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity):
        if item_name in self.items:       # if item already exist just increment the quantity
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
        print("Added {} of {} to the cart".format(quantity,item_name))

    def remove_item(self, item_name, quantity):
        if item_name in self.items:   #try to remove more quantity than already present,then delete alll
            if self.items[item_name]['quantity'] <= quantity:
                del self.items[item_name]
                print("Removed all {} from the cart".format(item_name))
            else:    #decrement the quantity 
                self.items[item_name]['quantity'] -= quantity
                print("Removed {} of {} from the cart".format(quantity,item_name))
        else:
            print("{} is not found in the cart".format(item_name))

    def calculate_total_price(self):
        total_price = 0
        for item in self.items.values():
            total_price += item['price'] * item['quantity']
        return total_price

    def display_cart(self):
        if not self.items:
            print("The cart i empty")
        else:
            print("Shopping Cart:")
            for item_name, item_info in self.items.items():
                print(f"{item_name}: {item_info['quantity']} x ${item_info['price']} = ${item_info['price'] * item_info['quantity']}")
            print("Total Cost:",cart.calculate_total_price())   #printing the total cost
# Create a shopping cart object
cart = ShoppingCart()

# Add items to the cart
cart.add_item("Apple", 100, 2)
cart.add_item("Banana", 50, 3)
cart.add_item("Orange", 150, 1)

# Display the cart
cart.display_cart()

# Remove an item from the cart
cart.remove_item("Banana", 1)

# Display the cart again
cart.display_cart()
