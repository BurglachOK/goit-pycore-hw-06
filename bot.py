from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
     def __init__(self, name: str):
        if not name:
            print(ValueError("Name cannot be empty."))
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone: str):
        if len(phone) <= 9:
            print(ValueError("Phone number must be at least 10 characters long"))
        super().__init__(phone)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone: str):
        if phone not in self.phones:
            self.phones.append(Phone(phone))


    def change_phone(self, old_phone: str, new_phone: str):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = Phone(new_phone)
        print('Please provide a valid phone number.')


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
        

        def new_record(self, name: str):
            if name not in self.data:
                self.data[name] = Record(name)
            return self.data[name]
        
        
        def add_record(self, name: str, phone = ''):
            record = self.new_record(name)
            if len(phone) > 9:
                record.add_phone(phone)
                return record
            print(ValueError("Phone number must be at least 10 characters long"))
            return None


        def get_records(self):
            for name, record in book.data.items():
                yield record


        def change_record(self, name: str, phone: str):
            if name in self.data:
                record = self.data[name]
                record.add_phone(phone)


        def __str__(self):
            return "\n".join(str(record) for record in self.data.values())
        

        def get_contact(self, name: str):
            if name in self.data:
                print(self.data[name])
            else:
                print(KeyError(f"Contact {name} not found."))








book = AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found." 
        except IndexError:
            return "Enter user name."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args):
    name, phone = args
    if phone not in book.data:
        if book.add_record(name, phone) is not None:
            return "Contact added."


@input_error
def change_contact(args):
    name, old_phone, new_phone = args
    if   name in book.data:
        book.change_record(name, phone)
        return "Contact updated."
    return "Contact not found."


@input_error
def show_phone(args):
    name = args[0]
    book.get_contact(name)
    return "Contact not found."


@input_error
def show_all():
    if book.data:
        book.get_records()
    else:
        return "No contacts found."


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()