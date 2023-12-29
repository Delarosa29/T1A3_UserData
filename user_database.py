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
    # \n starts new line
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


# Function for find a contact
def find_contact():
    os.system("clear")
    print("Enter the email address of the contact to find: ")
    email = input().strip()
    os.system("clear")
    print(f"\nValue of email: {email}")
    # Loads contacts from json 
    contacts = load()
    found = False
    # Find the contact with the matching email
    for contact in contacts:
        if contact.get("email").lower() == email.lower():
            # If email match = true, will display information 
            found = True
            # Displays details on screen
            print('\nContact Details Found:\n')
            print('First Name:', contact.get('first_name'))
            print('Last Name:', contact.get('last_name'))
            print('Mobile:', contact.get('mobile'))
            print('Email:', contact.get('email'))
            input('\nHit ENTER key to continue...')
            break
    
    # If found remains false, will then print invalid email
    if not found:
        print(f"Unable to find contact with email - {email}")
        input('\nHit ENTER key to continue...')
    return


# Function for update a contact
def update_contact(email):
    os.system("clear")  
    contacts = load()
    found = False
    
    # Goes over list of existing contacts
    for i, contact in enumerate(contacts):
        # If email matches, will begin input prompt to update info
        if contact["email"] == email:
            found = True
            
            # Prompt to update user info
            print("Enter new contact details:\n")
            print("First Name: ", end="")
            first_name = input()
            print("Last Name: ", end="")
            last_name = input()
            print("Mobile Number: ", end="")
            mobile = input()
            
            # Update the contact in the list
            contacts[i] = {
                "first_name": first_name,
                "last_name": last_name,
                "mobile": mobile,
                "email": email                
            }
            os.system("clear")

            # Displays the old entry info
            print("\nPrevious Entry:")
            print("First Name:", contact.get("first_name"))
            print("Last Name:", contact.get("last_name"))
            print("Mobile:", contact.get("mobile"))
            print("Email:", contact.get("email"))
            print("\nUpdated Entry:")
            
            # Displays updated info
            print("First Name:", first_name)
            print("Last Name:", last_name)
            print("Mobile:", mobile)
            print("Email:", email)
            print("\nContact updated successfully.")
            input("\nPress Enter to continue...")
            dump(contacts)  # Save the updated contacts to the file
            break

    # If email does not match, prompt user back to menu selection
    if not found:
        print(f"Unable to find contact with email: {email}")
        input("\nPress Enter to continue...")
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
            find_contact()
            continue
        # Update existing contact
        elif int_choice == 3:
            os.system("clear")
            print("Update contact was selected")
            print("\nEnter email of contact to update: ")
            email = input()
            update_contact(email)
            continue
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