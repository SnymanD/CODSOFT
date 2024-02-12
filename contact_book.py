# Contact Information: Store name, phone number, email, and address for each contact
# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers
# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.

contacts = {}

print("___________CONTACTS BOOK____________")
print("")


def display_contacts():
    print("____Contacts List____")
    for key in contacts:
        print(f"{key}{contacts.get(key)}")


while True:

    print("___Choose the option that you want___")
    choice = input("1. Add New Contact \n "
                   "2. Search Contact \n "
                   "3. Lists Contacts \n "
                   "4. Update Contact \n "
                   "5. Delete Contact \n "
                   "6. Quit \n"
                   ">>>"
                   )

    if choice == "1":
        name = input("Enter a name: ").capitalize()
        email = input("Enter an email address: ")
        address = input("Enter the home address: ")
        phone_number = input("Enter the mobile numbers: ")
        contacts["-"] = f"Name: {name}\n Phone Number: {phone_number} \n Email: {email} \n Address: {address} \n"
        print(f"{name} is added to your contacts")
        print("")

    elif choice == "2":
        search_contact = input("Enter the name of the contact: ")
        if search_contact in contacts:
            print(f"{search_contact}{contacts}")
        else:
            print("Contacts not found!")
            print("")

    elif choice == "3":
        if not contacts:
            print("Contact book is empty")
        else:
            display_contacts()
            print("")

    elif choice == "4":
        while True:
            update_contact = input("Enter the name of the contact you want to update: ").capitalize()
            if update_contact in contacts:
                choose = int(input(f"{1}. Update email \n "
                                   f"{2}. Update address \n"
                                   f"{3}. Update phone numbers \n"
                                   f"{4}. Quit \n"
                                   ">>>"))
                if choose == 1:
                    new_email = input("Enter a new email: ").capitalize()
                    contacts[new_email] = new_email
                    print("Email Address Updated")
                    display_contacts()

                elif choose == 2:
                    address = input("Enter New Address: ")
                    contacts[address] = address
                    print("Address Updated")

                elif choose == 3:
                    phone_number = input("Enter New Phone Numbers: ")
                    contacts[phone_number] = phone_number
                    print("Phone Numbers Updated")

                elif choose == 4:
                    break
            else:
                print("Contact not found!")

    elif choice == "5":
        delete_contact = input("Enter The Name Of The Contact To Delete")
        if delete_contact in contacts:
            contacts.pop(delete_contact)
        else:
            print("Contact not Found!")

    elif choice == "6":
        break
    if choice != ("1" or "2" or "3" or "4" or "5" or "6"):
        print("Invalid Choice!")

print("Goodbye")
