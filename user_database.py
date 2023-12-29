import os
# Imports json file for library
import json


# Checks if input choice is valid
def is_choice_valid(arg):
    try:
        int_val = int(arg)
        # Sets the range for menu selection
        if 1 <= int_val <= 6:
            return True
        return False 
    # For error handling
    except ValueError as ve:
        return False
    except BaseException as be:
        return False
    

# Opens or create json file and flush the contacts into json file (as str).
def dump(contacts):
    with open("./simple_db.json", "w") as simple_db:
        simple_db.write(json.dumps(contacts))


# load the contacts into the memory (as dict)
def load():
    filename = "./simple_db.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            contacts = file.read()
            if contacts is None or len(contacts) == 0:
                return []
            else:
                return json.loads(contacts)
    else:
        with open(filename, "w") as file:
            return []
        

# Function for creating new contact
def create_new_contact():
    # Clears terminal
    os.system("clear")
    header = "Adding New Contact"
    print("-" * len(header))
    print(header)
    print("-" * len(header), "\n")
    # Starts input for user info
    print("Enter First Name: ")
    first_name = input()
    print("Enter Last Name: ")
    last_name = input()
    print("Enter Mobile Number: ")
    mobile = input()
    print("Enter Email Address: ")
    email = input()

    # Creates library entries
    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "mobile": mobile,
        "email": email,
    }

    # Shows new entry info
    print(f"Adding new contact details: {contact}")
    
    try:
        # Retrieve the contacts data
        contacts = load()
        # Append the new contact to the database in memory
        contacts.append(contact)
        # Flush the database into the filesystem
        dump(contacts)
    except BaseException as be:
        print(f"Error occurred: {be=}, {be}")
    return


while True:
# Use Case - Main Screen
    os.system("clear")
    # Title header
    header = "Simple Database"
    # Prints line along header
    print("-" * len(header))
    print(header)
    print("-" * len(header), "\n")

    # Display list of options for user 
    print("1. Create new contact")
    print("2. Retrieve a contact by email")
    print("3. Update a contact by email")
    print("4. Delete a contact by email")
    print("5. Show Database Contents")
    print("6. Exit\n")


    choice = input()
    if is_choice_valid(choice):
        int_choice = int(choice)
        # Create new contact
        if int_choice == 1:
            print("Create contact was selected")
            # Calls on create contact function
            create_new_contact()
            continue
        # Find contact
        elif int_choice == 2:
            print("Find contact was selected")
            pass
        elif int_choice == 3:
            print("Update contact was selected")
            print("\nEnter email of contact to update: ")
            pass
        # Delete contact
        elif int_choice == 4:
            print("Delete contact was selected")
            pass
        elif int_choice == 5:
            print("Showing Database Contents")
            pass
        elif int_choice == 6:
            print("Exit was selected; Goodbye!")
            break
    else:
        print(f"Invalid choice - {choice}; try again...")
        continue