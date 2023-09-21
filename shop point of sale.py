import getpass

class Shop:
    def __init__(self):
        self.products = {
            "apple": {"price": 0.5, "quantity": 10},
            "banana": {"price": 0.25, "quantity": 10},
            "orange": {"price": 0.75, "quantity": 10},
            "grape": {"price": 1.0, "quantity": 10},
        }
        self.shopping_cart = []

    def display_available_products(self):
        print("Available Products:")
        for product, info in self.products.items():
            print(f"{product.capitalize()}: ${info['price']}, Quantity: {info['quantity']}")

    def add_to_cart(self, item):
        if item in self.products:
            if self.products[item]["quantity"] > 0:
                self.shopping_cart.append(item)
                self.products[item]["quantity"] -= 1
                print(f"{item.capitalize()} has been added to your cart.")
            else:
                print(f"Sorry, {item.capitalize()} is out of stock.")
        else:
            print("Invalid product. Please choose from the available products.")

    def checkout(self):
        total_cost = sum(self.products[item]["price"] for item in self.shopping_cart)
        print("\nYour Shopping Cart:")
        for item in self.shopping_cart:
            print(item.capitalize())
        print(f"Total Cost: ${total_cost:.2f}")
        print("\nThank you for shopping with us!")

    def save_shopping_cart(self, filename):
        with open(filename, 'w') as file:
            file.write("Shopping Cart:\n")
            for item in self.shopping_cart:
                file.write(f"{item.capitalize()}\n")
            file.write(f"Total Cost: ${sum(self.products[item]['price'] for item in self.shopping_cart):.2f}")

class Admin:
    def __init__(self):
        self.admin_password = "123"

    def add_new_product(self, shop, admin_password_input):
        if admin_password_input == self.admin_password:
            new_product_name = input("Enter the name of the new product: ").lower()
            new_product_price = float(input(f"Enter the price of {new_product_name.capitalize()}: "))
            new_product_quantity = int(input(f"Enter the initial quantity of {new_product_name.capitalize()}: "))

            if new_product_name in shop.products:
                print(f"{new_product_name.capitalize()} already exists in the system. Use 'edit' to modify the product.")
                return

            shop.products[new_product_name] = {"price": new_product_price, "quantity": new_product_quantity}
            print(f"{new_product_name.capitalize()} has been added to the system.")
        else:
            print("Incorrect password. Only the admin can add a new product.")

if __name__ == "__main__":
    shop = Shop()
    admin = Admin()

    while True:
        action = input("Enter 'add' to add a product to your cart, 'new' to add a new product, 'save' to save your cart, or 'done' to finish shopping: ").lower()

        if action == 'done':
            break
        elif action == 'add':
            shop.display_available_products()
            item = input("Enter a product to add to your cart or 'finish': ").lower()
            while item != 'finish':
                shop.add_to_cart(item)
                item = input("Enter a product to add to your cart or 'finish': ").lower()

        elif action == 'new':
            admin_password_input = getpass.getpass("Enter the admin password: ")
            admin.add_new_product(shop, admin_password_input)
        elif action == 'save':
            filename = input("Enter the filename to save your shopping cart: ")
            shop.save_shopping_cart(filename)
            print(f"Shopping cart saved to {filename}")
        else:
            print("Invalid action. Please enter 'add', 'new', 'save', or 'done'.")

    shop.checkout()
