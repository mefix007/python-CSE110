# Shopping cart
cart = []

def add_item():
    item = input("Enter the item you want to add: ")
    cart.append(item)
    print(f"{item} has been added to the shopping cart.")


def display_cart():
    if len(cart) == 0:
        print("The shopping cart is empty.")
    else:
        print("Contents of the shopping cart:")
        for item in cart:
            print(item)

def remove_item():
    item = input("Enter the item you want to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"{item} has been removed from the shopping cart.")
    else:
        print(f"{item} is not in the shopping cart.")

def compute_total():
    # Placeholder function for computing the total
    print("Computing total...")  # Replace with your own implementation

def menu():
    while True:
        print("\nMenu:")
        print("1. Add a new item")
        print("2. Display the contents of the shopping cart")
        print("3. Remove an item")
        print("4. Compute the total")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_item()
        elif choice == "2":
            display_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            compute_total()
        elif choice == "5":
            print("Thank you for using the shopping cart!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
menu()