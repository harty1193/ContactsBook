import pickle

class ContactDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = {}

    def load_contacts(self):
        try:
            with open(self.file_path, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = {}

    def save_contacts(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.contacts, file)
