# Shopping cart for Mefix groceries store
print()

print("Welcome to mefix groceries stores \nIn order to serve you better \npls select the options that matches your needs from the menu option")
cart = []

def add_item():
    item = input("Enter the item you want to add: ")
    price = float(input("Enter the price of the item: "))
    cart.append((item, price))
    print(f"{item} has been added to the shopping cart.")

def display_cart():
    if len(cart) == 0:
        print("The shopping cart is empty.")
    else:
        print("Contents of the shopping cart:")
        for i, (item, price) in enumerate(cart, start=1):
            print(f"{i}. {item} - ${price:.2f}")

def remove_item():
    if len(cart) == 0:
        print("The shopping cart is empty. Nothing to remove.")
        return

    display_cart()
    choice = int(input("Enter the number of the item to remove: ")) - 1

    if choice < 0 or choice >= len(cart):
        print("Invalid item number. Please try again.")
    else:
        item, price = cart.pop(choice)
        print(f"{item} has been removed from the shopping cart.")

def calculate_total():
    if len(cart) == 0:
        print("The shopping cart is empty. Total price: $0.00")
    else:
        total = sum(price for _, price in cart)
        print(f"Total price: ${total:.2f}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add a new item")
        print("2. Display the contents of the shopping cart")
        print("3. Remove an item")
        print("4. Calculate the total")
        print("5. Quit")
        print()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_item()
        elif choice == "2":
            display_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            print()
            print("Thank you for patronizing Mefix groceries store")
            break
        else:
            print("Invalid choice. Please try again.")
# Start the program
menu()