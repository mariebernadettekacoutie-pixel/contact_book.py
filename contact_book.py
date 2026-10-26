
def add_contact(contacts):
    name = input("Enter contact name: ").strip()

    if not name:
        print("Error: Name cannot be empty.")
        return

    # Check for an existing name, ignoring capitalization
    for existing_name in contacts:
        if existing_name.lower() == name.lower():
            print("This contact already exists!")
            return

    phone = input("Enter phone number: ").strip()

    # Allow digits and an optional leading +
    if not phone or not phone.lstrip("+").isdigit():
        print("Invalid phone number. Use digits and an optional +.")
        return

    contacts[name] = phone
    print(f"Contact '{name}' added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("Your contact list is empty.")
        return

    print("\n--- All Contacts ---")
    for name in sorted(contacts, key=str.lower):
        print(f"Name: {name} | Phone: {contacts[name]}")


def search_contact(contacts):
    search_name = input("Enter a name or part of a name: ").strip()

    if not search_name:
        print("Please enter a name to search.")
        return

    matches = [
        (name, phone)
        for name, phone in contacts.items()
        if search_name.lower() in name.lower()
    ]

    if matches:
        print("\n--- Search Results ---")
        for name, phone in matches:
            print(f"Name: {name} | Phone: {phone}")
    else:
        print("No matching contact found.")


def delete_contact(contacts):
    name = input("Enter the name to delete: ").strip()

    # Find the stored name, ignoring capitalization
    matching_name = next(
        (existing for existing in contacts
         if existing.lower() == name.lower()),
        None
    )

    if matching_name is not None:
        del contacts[matching_name]
        print(f"Contact '{matching_name}' deleted successfully!")
    else:
        print("Contact not found.")


def main():
    contacts = {}

    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            print("Thank you for using Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
