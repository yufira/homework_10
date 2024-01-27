from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Invalid phone number format')
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            new_number = Phone(phone)
            self.phones.append(new_number)
        except ValueError as e:
            print(f'Error adding phone number: {e}')

    def remove_phone(self, phone):
        phones_to_remove = filter(lambda p: p.value == phone, self.phones)
        for phone in phones_to_remove:
            self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        found = False
        if not new_number.isdigit() or len(new_number) != 10:
            raise ValueError('Invalid phone number format')
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                found = True
                break

        if not found:
            raise ValueError(
                f"Phone number '{old_number}' not found in the record."
                )

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {'; '.join(p.value for p in self.phones)}"
        )


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
