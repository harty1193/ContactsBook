from model import Contact
from database import ContactDatabase

class ContactViews:
    def __init__(self, file_path):
        self.contact_db = ContactDatabase(file_path)
        self.contact_db.load_contacts()

    def display_contacts(self):
        if self.contact_db.contacts:
            for contact_name, contact in self.contact_db.contacts.items():
                print(contact)
        else:
            print("No contacts found.")

    def add_contact(self, first_name, last_name, email, phone='', job_title='', address=''):
        contact = Contact(first_name, last_name, email, phone, job_title, address)
        contact_name = f"{first_name} {last_name}"
        self.contact_db.contacts[contact_name] = contact
        self.contact_db.save_contacts()

    def search_contacts(self, field, value):
        results = []
        for contact_name, contact in self.contact_db.contacts.items():
            if getattr(contact, field, None) == value:
                results.append(contact)
        return results

    def edit_contact(self, contact_name, field, new_value):
        contact = self.contact_db.contacts.get(contact_name)
        if contact:
            setattr(contact, field, new_value)
            self.contact_db.save_contacts()
            return True
        return False

    def delete_contact(self, contact_name):
        if contact_name in self.contact_db.contacts:
            del self.contact_db.contacts[contact_name]
            self.contact_db.save_contacts()
            return True
        return False
