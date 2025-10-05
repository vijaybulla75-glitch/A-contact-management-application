import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"\n{i}. Name: {c['name']}\n   Phone: {c['phone']}\n   Email: {c['email']}\n   Address: {c['address']}")

# Search contact by name or phone
def search_contact():
    search_term = input("Enter name or phone to search: ").lower()
    contacts = load_contacts()
    found = [c for c in contacts if search_term in c['name'].lower() or search_term in c['phone']]
    if found:
        for c in found:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
    else:
        print("❌ No contact found.")

# Edit contact
def edit_contact():
    name = input("Enter the name of the contact to edit: ").lower()
    contacts = load_contacts()
    for c in contacts:
        if c['name'].lower() == name:
            print("Leave blank to keep old value.")
            new_phone = input(f"New phone ({c['phone']}): ") or c['phone']
            new_email = input(f"New email ({c['email']}): ") or c['email']
            new_address = input(f"New address ({c['address']}): ") or c['address']
            c.update({"phone": new_phone, "email": new_email, "address": new_address})
            save_contacts(contacts)
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

# Delete contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['name'].lower() != name]
    if len(new_contacts) != len(contacts):
        save_contacts(new_contacts)
        print("🗑️ Contact deleted successfully.")
    else:
        print("❌ Contact not found.")

# Main menu
def main():
    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
