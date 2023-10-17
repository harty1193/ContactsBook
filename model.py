class Contact:
    def __init__(self, first_name, last_name, email, phone='', job_title='', address=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.job_title = job_title
        self.address = address

    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}, Phone: {self.phone}, Job Title: {self.job_title}, Address: {self.address}"