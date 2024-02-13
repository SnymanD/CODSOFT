# Contact Information: Store name, phone number, email, and address for each contact
# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers
# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.

contacts = {}
print("__________CONTACTS BOOK__________")
print("")


def display_contacts():
    print("___Contacts List___")
    for key in contacts:
        print(f"{key}{contacts.get(key)}")


while True:
    print("Choose to perform an action: ")
    choice = int(input(f"{1} List All The Contacts \n"
                       f"{2} Add New Contact \n"
                       f"{3} Search A Contact \n"
                       f"{4} Update A Contact \n"
                       f"{5} Delete A Contact \n"
                       f"{6} Quit \n"
                       ">>>"))

    if choice == 1:
        if not contacts:
            print("Contact book is currently empty!")
            print("")
        else:
            display_contacts()

    elif choice == 2:
        name = input("Please enter a name of the person: ").capitalize()
        email = input("Please enter an email address of the person: ")
        address = input("Please enter the home of address of the person: ")
        mobile_number = int(input("Please enter the mobile number: "))
        print(f"{name} is added to your contacts")
        print("")
        contacts["-"] = f"Name: {name}\n Email: {email}\n Address: {address}\n Mobile: {mobile_number}\n"
        
    elif choice == 3:
        search_contact = input("Please enter the name of the contact to search: ").capitalize()
        if search_contact not in contacts:
            print("Contact name not found!")
        else:
            print(contacts[search_contact])
            print("")

    elif choice == 4:
        update_contact = input("Please enter the name of the contact to update: ").capitalize()
        if update_contact in contacts:
            print("What would you like to do?")
            choose = int(input(f"{1} Change the email address \n"
                               f"{2} Change the home address \n"
                               f"{3} Change the mobile number \n"
                               f"{4} Update the name \n"
                               f"{5} Quit \n"))
            if choose == 1:
                new_email = input("Please enter a new email address:")
                contacts[0] = new_email
                display_contacts()
            elif choose == 2:
                address = input("Please enter a new email address:")
                contacts[address] = address
                display_contacts()
            elif choose == 3:
                mobile_number = int(input("Enter a new mobile number: "))
                contacts[mobile_number] = mobile_number
                display_contacts()
            elif choose == 4:
                name = input("Please enter a new name: ").capitalize()
                contacts[name] = name
                display_contacts()
            elif choose == 5:
                break

        elif choice == 5:
            delete_contact = input("Enter the name of the contact to delete: ").capitalize()
            if delete_contact in contacts:
                contacts.pop(delete_contact)
                display_contacts()
            else:
                print("Contact not found!")

    elif choice == 6:
        break
