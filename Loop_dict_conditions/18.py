inventory = {}

while True:
    print("\nGrocery Inventory Menu")
    print("1. Add a new product")
    print("2. Restock an existing product")
    print("3. Sell a product")
    print("4. Display all products and stock values")
    print("5. Display total inventory value")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ").strip()
        if product in inventory:
            print("Product already exists.")
            continue

        while True:
            try:
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter valid numeric values.")
                continue

            if price < 0:
                print("Price cannot be negative.")
                continue
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue

            inventory[product] = {"price": price, "quantity": quantity}
            print("Product added.")
            break

    elif choice == "2":
        product = input("Enter product name to restock: ").strip()
        if product not in inventory:
            print("Product not found.")
            continue

        while True:
            try:
                amount = int(input("Enter quantity to add: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if amount < 0:
                print("Quantity cannot be negative.")
                continue

            inventory[product]["quantity"] += amount
            print("Stock updated.")
            break

    elif choice == "3":
        product = input("Enter product name to sell: ").strip()
        if product not in inventory:
            print("Product not found.")
            continue

        while True:
            try:
                amount = int(input("Enter quantity to sell: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if amount < 0:
                print("Quantity cannot be negative.")
                continue
            if amount > inventory[product]["quantity"]:
                print("Not enough stock to sell that quantity.")
                continue

            inventory[product]["quantity"] -= amount
            print("Sale completed.")
            break

    elif choice == "4":
        print("\nProducts and stock values:")
        for product, details in inventory.items():
            print(f"{product}: price = {details['price']}, quantity = {details['quantity']}, stock value = {details['price'] * details['quantity']}")

    elif choice == "5":
        total_value = 0
        for product, details in inventory.items():
            total_value += details["price"] * details["quantity"]
        print(f"Total inventory value: {total_value}")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
