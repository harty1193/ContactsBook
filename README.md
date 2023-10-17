#ContactsBook Application
In Python

##Overview
The ContactsBook application is a Python program designed to help users create, store, manage, and interact with a list of contacts. This application uses a command-line interface (CLI) to provide various functionalities for managing contact information. It allows users to add new contacts, search for existing contacts, edit contact details, delete contacts, display all contacts, and save/restore the contact list to/from a file. The program is organized into separate modules within a directory structure, making it easy to maintain and expand.

#Directory Structure
The ContactsBook application is organized into the following directory structure:
contacts_project/
│
└──ContactsBook3.0/
|	└── main.py 
│	└── database.py
| └── views.py
│	└── main.py
│	└── model.py
|	└── contacts.py

##Requirement:
termcolor py module. <br>
command to install.
`pip install termcolor`

Each component serves a specific purpose within the application:
<ul>
<li><b>model.py:</b> Defines the Contact class to structure contact information.</li>
<li><b>database.py:</b> Manages the storage and retrieval of contacts using a dictionary data structure and pickle files.</li>
<li><b>views.py:</b> Provides user interaction and a menu system, allowing users to input choices and interact with contacts.</li>
<li><b>main.py:</b> The main entry point for the application, where the user interacts with the ContactsBook and initiates contact-related actions.</li>
<li><b>contacts.py:</b> The primary entry point for running the application.
</ul>

Features
1. Add a New Contact
Users can add new contacts by providing details such as First Name, Last Name, Email, Phone, Job Title, and Address. Contacts must have at least a First Name and Email.
2. Search for an Existing Contact
Users can search for existing contacts using various criteria, such as First Name, Last Name, Email, Phone, and Job Title. The application can return multiple entries if multiple contacts match the criteria.
3. Edit an Existing Contact
Users can edit the details of an existing contact, including fields such as First Name, Last Name, Email, Phone, and Job Title. After making changes, the program asks for confirmation to save the edited contact.
4. Delete a Contact
Users can delete an existing contact from the list.
5. Display All Contacts
The program can display the details of all stored contacts.
6. Save and Restore Contact List
Contacts are saved into a pickle file when exiting the program. The program also prompts users for a file path to save/update the pickle file. When the program is restarted, it restores the previously saved contact list.

Colorization
The menu and user prompts are colorized using the termcolor library, enhancing the user interface and providing a better visual experience.

Usage
To run the ContactsBook application, execute the contacts.py script. Upon startup, the program will ask for the file path to save the contact data. Users can then interact with the application by selecting options from the menu.

Conclusion
The ContactsBook application is a versatile tool for managing and organizing contact information. With a clear directory structure, easy-to-use menu system, and colorful interface, it offers an intuitive and visually pleasing way to handle contact-related tasks.
