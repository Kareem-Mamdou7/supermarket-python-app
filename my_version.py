import json


class Supermarket:
    def __init__(self):
        self.products_json_file_path = "./Supermarket System OOP/products.json"

        with open(self.products_json_file_path, "r") as f:
            self.products = json.load(f)

        self.cart = []
        self.total_price = 0

    # ----------------------------
    # Utility Methods
    # ----------------------------
    def is_store_empty(self):
        return len(self.products) == 0

    def is_product_in_store(self, name):
        return any(product["name"] == name for product in self.products)

    def get_product_quantity(self, name):
        for product in self.products:
            if product["name"] == name:
                return product["quantity"]
        return 0  # default if not found

    def get_total_cost(self):
        if self.cart:
            total_cost = 0

            for product in self.cart:
                total_cost += product["price"] * product["quantity"]

            return total_cost

        return 0

    def update_products_json(self):
        with open(self.products_json_file_path, "w") as file:
            json.dump(self.products, file, indent=2)

    # ----------------------------
    # Store Management
    # ----------------------------
    def add_product(self, name, price, quantity=10):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        name = name.lower().strip()

        if not self.is_product_in_store(name):
            product = {"name": name, "price": price, "quantity": quantity}
            self.products.append(product)
            print(f"Added '{name}' to the supermarket.\n")

        else:
            for product in self.products:
                if product["name"] == name:
                    is_same_price = product["price"] == price
                    product["quantity"] += quantity

                    if not is_same_price:
                        product["price"] = price

                    print(
                        f"Product Was Already In Store,\nUpdated Stock Number:{product["quantity"]}\n"
                    )

                    if not is_same_price:
                        print(f"Updated Price: {price:.2f}$")

        self.update_products_json()

    def remove_product(self, name):
        name = name.strip().lower()

        if self.is_store_empty():
            print("There's no products in the supermarket.")
            return

        if not self.is_product_in_store(name):
            print("Product Not Found in Supermarket.")
            return

        self.products = [p for p in self.products if p["name"] != name]
        print(f"Removed '{name}' from the supermarket.\n")
        self.update_products_json()

    def display_products(self):
        if self.is_store_empty():
            print("There's no products in the supermarket yet\n")
        else:
            print("=" * 30)
            print("List of Products:")
            print("-" * 30)
            for product in self.products:
                print(f"name:      {product['name']}")
                print(f"price:     {product['price']:.2f}$")
                print(f"quantity:  {product['quantity']}")
                print("-" * 30)
            print("=" * 30)
            print()

    # ----------------------------
    # Cart Management
    # ----------------------------
    def add_to_cart(self, name):
        name = name.strip().lower()

        if self.is_store_empty():
            print("There's no products in the supermarket.")
            return

        if not self.is_product_in_store(name):
            print("Product Not Found in Supermarket.")
            return

        available = self.get_product_quantity(name)

        quantity = int(
            input(f"How many '{name}' do you want?\nAvailable: {available}\n\n")
        )

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        # (default fallback removed — user must enter a number)

        if available < quantity:
            print(f"Insufficient Quantity in Store. Available: {available}")
            return

        # Deduct from store
        price = 0.00
        for product in self.products:
            if product["name"] == name:
                product["quantity"] -= quantity
                price = product["price"]

        for item in self.cart:
            if item["name"] == name:
                item["quantity"] += quantity
                break

        else:
            self.cart.append({"name": name, "price": price, "quantity": quantity})

        print(
            f"Added x{quantity} of '{name}' to your cart! Remaining in store: {self.get_product_quantity(name)}"
        )
        print(f"Total Cost Of Product Added: {quantity * price:.2f}$\n")

        # Remove from store if stock hits zero
        if self.get_product_quantity(name) == 0:
            self.remove_product(name)

        self.update_products_json()

    def remove_from_cart(self, name):
        name = name.strip().lower()
        availabe_in_cart = None

        if not self.cart:
            print("Your cart is empty.")
            return

        if not any(product["name"] == name for product in self.cart):
            print("Product is not in the cart.")
            return

        for product in self.cart:
            if product["name"] == name:
                availabe_in_cart = product["quantity"]

        quantity_to_remove = int(
            input(
                f"What's the amount you want to remove?\nAvailable: {availabe_in_cart}\n\n"
            )
        )

        if quantity_to_remove <= 0:
            print("Quantity must be greater than 0.")
            return

        for product in self.cart:
            if product["name"] == name:
                # removed: if quantity_to_remove is None (no longer used)

                if product["quantity"] < quantity_to_remove:
                    print("You picked more than what's in the cart.")
                    return

                # Return items back to store
                self.add_product(name, product["price"], quantity_to_remove)

                # Update cart
                if product["quantity"] == quantity_to_remove:
                    self.cart = [p for p in self.cart if p["name"] != name]
                else:
                    product["quantity"] -= quantity_to_remove

                print(
                    f"Removed x{quantity_to_remove} of '{name}' from your cart. Returned to store."
                )

                self.update_products_json()
                return

    def display_cart(self):
        if not self.cart:
            print("There's no products in the cart yet\n")

        else:
            print("=" * 30)
            print("Your Cart:")
            print("-" * 30)
            for product in self.cart:
                print(f"name:      {product['name']}")
                print(f"price:     {product['price']:.2f}$")
                print(f"quantity:  {product['quantity']}")
                print("-" * 30)
            print("=" * 30)
            print()

    def checkout(self):
        if self.cart:
            amount_paid = float(
                input(
                    f"You owe us: {self.get_total_cost():.2f}$\nEnter the amount to pay: "
                )
            )

            if amount_paid < self.get_total_cost():
                print("Insufficient Amount!")

            else:
                change = amount_paid - self.get_total_cost()

                print(f"Transaction Successful!\nHere's Your Change: {change:.2f}$")

                with open("./Supermarket System OOP/transactions.txt", "a") as f:
                    name_w = 15
                    price_w = 5
                    qty_w = 12
                    total_w = name_w + price_w + qty_w

                    f.write("=========== CHECKOUT ===========\n")

                    f.write(
                        f"{'Name':<{name_w}}{'Price':>{price_w}}{'Quantity':>{qty_w}}\n"
                    )

                    f.write("=" * total_w + "\n")
                    for product in self.cart:
                        f.write(
                            f"{product['name']:<{name_w}}{product['price']:>{price_w}.2f}{product['quantity']:>{qty_w}}\n"
                        )
                        f.write("-" * total_w + "\n")

                    f.write("*" * total_w + "\n")
                    f.write(
                        f"{'total price:':<{total_w-10}}{self.get_total_cost():>9.2f}$\n"
                    )
                    f.write(f"{'amount paid:':<{total_w-10}}{amount_paid:>9.2f}$\n")
                    f.write(f"{'change:':<{total_w-10}}{change:>9.2f}$\n")
                    f.write("=" * total_w + "\n\n")

                self.cart = []

        else:
            print("There's Nothing in the cart yet!")


x = Supermarket()

print("Welcome To Kareem's Market!")

while True:
    choice = int(
        input(
            "\nWhat Do You Want To Do?\n(1) Display Store Products. (Stock)\n(2) Add Product To Store.\n(3) Remove Product from Store\n(4) Display Cart.\n(5) Add Product To Cart.\n(6) Remove Product From Cart.\n(7) Checkout.\n(8) Read Transactions' File.\n(9) Exit.\n\n"
        )
    )

    match choice:
        case 1:
            x.display_products()

        case 2:
            name = input("Enter New Product's Name: ")
            price = float(input("Enter New Product's Price: "))
            quantity = int(input("Enter New Product's Quantity: "))

            x.add_product(name, price, quantity)

        case 3:
            name = input("Enter New Product's Name You Want To Remove: ")

            x.remove_product(name)

        case 4:
            x.display_cart()

        case 5:
            x.display_products()

            name = input("Enter Product's Name To Add To Cart: ")

            x.add_to_cart(name)

        case 6:
            name = input("Enter Product's Name To Remove From Cart: ")

            x.remove_from_cart(name)

        case 7:
            x.checkout()

        case 8:
            with open("./Supermarket System OOP/transactions.txt", "r") as f:
                print(f.read())

        case 9:
            print("Ok, Goodbye!")
            break

        case _:
            print("Invalid Input, Please Pick Between (1 - 9)")
