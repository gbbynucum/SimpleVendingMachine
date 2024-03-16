class VendingMachine:
    def __init__(self):
        self.products = {
            "Coke": 34,
            "Pepsi": 30,
            "Royal": 32,
            "Coke Zero": 39,
            "Sprite": 38
        }
        self.balance = 0.0

    def display_products(self):
        print("\nAvailable Products:")
        for product, price in self.products.items():
            print(f"{product}: ₱{price:.2f}")

    def add_money(self, amount):
        self.balance += amount

    def buy_product(self, product_name):
        if product_name in self.products:
            price = self.products[product_name]
            if self.balance >= price:
                self.balance -= price
                print(f"Enjoy your {product_name}!")
            else:
                print("Insufficient funds. Please add more money.")
        else:
            print("Product not available.")

    def give_change(self):
        if self.balance > 0:
            print(f"Returning change: ₱{self.balance:.2f}")
            self.balance = 0.0


def main():
    vending_machine = VendingMachine()

    while True:
        print("\nWelcome to the Soft Drinks Vending Machine!")
        vending_machine.display_products()
        print(f"\nCurrent Balance: ₱{vending_machine.balance:.2f}")

        choice = input("\nEnter 'a' to add money, 'b' to buy a product, 'c' to exit: ").lower()

        if choice == 'a':
            amount = float(input("Enter amount to add: "))
            vending_machine.add_money(amount)
        elif choice == 'b':
            product_name = input("Enter the product name you want to buy: ")
            vending_machine.buy_product(product_name)
        elif choice == 'c':
            vending_machine.give_change()
            print("Thank you for using the Vending Machine!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
