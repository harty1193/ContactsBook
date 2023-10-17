from views import ContactViews
from termcolor import colored

def main():
    file_path = input(colored("Enter the file path to save the contact data (e.g., contacts.pkl): ", 'cyan'))
    views = ContactViews(file_path)

    while True:
        print(colored("\nContacts Application Menu:", 'cyan'))
        print("1. "+colored("Add a new contact", 'blue'))
        print("2. "+colored("Search for an existing contact", 'blue'))
        print("3. "+colored("Edit an existing contact", 'blue'))
        print("4. "+colored("Delete a contact", 'blue'))
        print("5. "+colored("Display All Contacts", 'blue'))
        print("6. "+colored("Exit", 'red'))

        choice = input(colored("Enter your choice: ", 'cyan'))

        if choice == '1':
            email = input(colored("Enter Email: ", 'cyan'))
            first_name = input(colored("Enter First Name: ", 'cyan'))
            if first_name and email:                
                last_name = input(colored("Enter Last Name: ", 'cyan'))
                phone = input(colored("Enter Phone: "))
                job_title = input(colored("Enter Job Title: ", 'cyan'))
                address = input(colored("Enter Address: ", 'cyan'))
                views.add_contact(first_name, last_name, email, phone, job_title, address)
            else:
                print(colored("Email and First Name are required", 'red'))

        elif choice == '2':
            print(colored("Search Options:", 'cyan'))
            print(colored("1. Search by First Name", 'blue'))
            print(colored("2. Search by Last Name", 'blue'))
            print(colored("3. Search by Email", 'blue'))
            print(colored("4. Search by Job Title", 'blue'))
            print(colored("5. Search by Phone", 'blue'))

            search_choice = input(colored("Enter your search choice: ", 'cyan'))

            if search_choice == '1':
                search_field = "first_name"
            elif search_choice == '2':
                search_field = "last_name"
            elif search_choice == '3':
                search_field = "email"
            elif search_choice == '4':
                search_field = "job_title"
            elif search_choice == '5':
                search_field = "phone"
            else:
                print(colored("Invalid search choice.", 'red'))
                continue

            search_value = input(colored(f"Enter the {search_field} to search for: ", 'cyan'))
            results = views.search_contacts(search_field, search_value)
            if results:
                print(colored("Search Results:", 'yellow'))
                for contact in results:
                    print(contact)
            else:
                print(colored("No matching contacts found.", 'red'))


        elif choice == '3':
            contact_name = input(colored("Enter the Contact name of the contact you want to edit: ", 'cyan'))
            
            if contact_name in views.contact_db.contacts:
                print(colored("Edit Options:", 'cyan'))
                print("1. "+colored("Edit First Name", 'blue'))
                print("2. "+colored("Edit Last Name", 'blue'))
                print("3. "+colored("Edit Email", 'blue'))
                print("4. "+colored("Edit Job Title", 'blue'))
                print("5. "+colored("Edit Phone", 'blue'))
                
                edit_choice = input("Enter your search choice: ")
            
                if edit_choice == '1':
                    edit_field = "first_name"
                elif edit_choice == '2':
                    edit_field = "last_name"
                elif edit_choice == '3':
                    edit_field = "email"
                elif edit_choice == '4':
                    edit_field = "job_title"
                elif edit_choice == '5':
                    edit_field = "phone"
                else:
                    print(colored("Invalid search choice.", 'red'))
                    continue
                    
                #field = input("Enter the field to edit (First Name, Last Name, Email, Phone, JobTitle): ")
                new_value = input(colored(f"Enter the new value for {edit_field}: ", 'cyan'))
                if views.edit_contact(contact_name, edit_field.lower(), new_value):
                    print(colored("Contact updated successfully.", 'green'))
                else:
                    print(colored("Failed to edit contact.", 'red'))
            else:
                print(colored("Contact not found.", 'red'))

        elif choice == '4':
            contact_name = input(colored("Enter the name of the contact you want to delete: ", 'magenta'))
            if views.delete_contact(contact_name):
                print(colored("Contact deleted successfully.", 'magenta'))
            else:
                print(colored("Contact not found.", 'red'))

        elif choice == '5':
            views.display_contacts()

        elif choice == '6':
            views.contact_db.save_contacts()
            print(colored("Contacts saved to", 'yellow'), file_path)
            print(colored("Goodbye!", 'green'))
            break

if __name__ == "__main__":
    main()
