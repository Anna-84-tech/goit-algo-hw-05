def input_error(func):
    """
    Decorator to handle user input errors such as KeyError, ValueError, and IndexError.
    Prevents the program from crashing and returns a helpful error message.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found. Please check the name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def add_contact(args, contacts):
    """Add a new contact to the contacts dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """Update an existing contact's phone number."""
    name, phone = args
    if contacts[name]:  
        contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    """Retrieve and return the phone number for a given contact name."""
    name = args[0]
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    """Return all contacts stored in the dictionary."""
    if not contacts:
        return "No contacts saved yet."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def parse_input(user_input):
    """Parse the user input string into a command and arguments."""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def main():
    """Main function to run the console assistant bot."""
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

# ==========================================
# Testing block to verify handler functions
# ==========================================
if __name__ == "__main__":
    # You can uncomment main() to run the interactive bot:
    main()
    
    # test_contacts = {}
    
    # print("--- Running Tests ---")
    
    # # Test 1: Successful addition
    # print(add_contact(["Bob", "0501234356"], test_contacts))  # Expected: Contact added.
    
    # # Test 2: ValueError (missing phone number argument)
    # print(add_contact(["Alice"], test_contacts))               # Expected: Give me name and phone please.
    
    # # Test 3: IndexError (missing argument for phone command)
    # print(show_phone([], test_contacts))                       # Expected: Enter the argument for the command.
    
    # # Test 4: Successful retrieval
    # print(show_phone(["Bob"], test_contacts))                  # Expected: Bob: 0501234356
    
    # # Test 5: KeyError (contact does not exist)
    # print(show_phone(["Charlie"], test_contacts))              # Expected: Contact not found. Please check the name.
    
    # # Test 6: Show all contacts
    # print(show_all(test_contacts)) 

    # # Test 7: Change non-existent contact (triggers natural KeyError)
    # print(change_contact(["Charlie", "1112223344"], test_contacts)) # Expected: Contact not found. Please check the name.