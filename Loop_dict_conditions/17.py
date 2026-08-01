contacts = {}

while True:
    print("\nContact Book Menu")
    print("1. Add or update a contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        print("\nAll contacts:")
        for name in sorted(contacts):
            print(f"{name}: {contacts[name]}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
