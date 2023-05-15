# Create an empty phone book dictionary
phone_book = {}

# Function to add a contact to the phone book
def add_contact():
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number: ")
    phone_book[name] = number
    print("Contact added successfully!")

# Function to remove a contact from the phone book
def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in phone_book:
        del phone_book[name]
        print("Contact removed successfully!")
    else:
        print("Contact not found in the phone book.")

# Function to display the phone book
def display_phone_book():
    if phone_book:
        print("Phone Book:")
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    else:
        print("Phone Book is empty.")

# Main program loop
while True:
    print("\n----- Menu -----")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Display the phone book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        display_phone_book()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
