from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
         super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('Value error.It`s not a phone number.')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
         self.phones.append(Phone(phone_number))
    
    def remove_phone(self, phone_number):
         for phone in self.phones:
              if str(phone) == phone_number:
                   self.phones.remove(phone)
              
    def edit_phone(self, phone_number, new_phone_number):
         for phone in self.phones:
              if str(phone) == phone_number:
                   self.phones[self.phones.index(phone)] = Phone(new_phone_number)
        

    def find_phone(self, phone_number):
         for phone in self.phones:
              if str(phone) == phone_number:
                   return phone         
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        del self.data[name]



     

