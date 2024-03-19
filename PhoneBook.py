def add_contact(phone_book, name, number):
    phone_book[name] = number
    print("Contact added successfully.")

def look_up_contact(phone_book, name):
    if name in phone_book:
        print(f"{name}'s phone number is {phone_book[name]}.")
    else:
        print("Contact not found.")

def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_menu():
    print("\nPhone Book:")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. Delete contact")
    print("4. Exit")

phone_book = {}

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        add_contact(phone_book, name, number)
    elif choice == "2":
        name = input("Enter contact name: ")
        look_up_contact(phone_book, name)
    elif choice == "3":
        name = input("Enter contact name: ")
        delete_contact(phone_book, name)
    elif choice == "4":
        print("Exiting the phone book.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
