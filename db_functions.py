import os
# Imports json file for library read and write
import json

# Clears terminal screen
def clear_screen():
    os.system("clear")


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
    

# Opens or create json file and flush the contacts into json file (as str)
def dump(contacts):
    # Opens file in write mode 
    with open("./simple_db.json", "w") as simple_db:
        # Writes JSON entry as string from python dictionary
        simple_db.write(json.dumps(contacts))


# load the contacts into the memory (as dict)
def load():
    # File name and path of json
    filename = "./simple_db.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            contacts = file.read()
            # Checks if there is any info
            if contacts is None or len(contacts) == 0:
                # Returns empty
                return []
            else:
                return json.loads(contacts)
    else:
        # Creates a file in write mode if file does not exist
        with open(filename, "w") as file:
            return []
        

# Function for creating new contact
def create_new_contact():
    # Clears terminal screen
    clear_screen()
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
    email = input().lower().strip()

    # Creates library entries in format
    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "mobile": mobile,
        "email": email,
    }
   
    try:
        # Retrieve the contacts data
        contacts = load()
        # Append the new contact to the database in memory
        contacts.append(contact)
        # Flush the database into the filesystem
        dump(contacts)
        # Confirmation screen
        clear_screen()
        print("\nNew contact added successfully:\n")
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Mobile:", mobile)
        print("Email:", email)
        input("\nPress ENTER to continue...")       
                       
    except BaseException as be:
        print(f"Error occurred: {be=}, {be}")
    return


# Function for find a contact
def find_contact():
    # Clears terminal screen
    clear_screen()
    print("Enter the email address of the contact to find: ")
    # .strip() Returns the input string while removing excess space
    email = input().lower().strip()
    clear_screen()
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


# Function to update a contact
def update_contact(email):
    # Clears terminal screen
    clear_screen()
    email = email.lower().strip()  
    contacts = load()
    found = False
    
    # Goes over list of existing contacts
    for i, contact in enumerate(contacts):
        # If email matches, will begin input prompt to update info
        if contact["email"] == email.lower():
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
            # Clears terminal screen
            clear_screen()

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


# Function to delete contact
def delete_contact():
    # Clears terminal screen
    clear_screen()
    # Displays current menu selection
    header = "Deleting Contact"
    print("-" * len(header))
    print(header)
    print("-" * len(header), "\n")
    print("Enter Email Address of the Contact to Delete: ")
    # .strip() Returns the input string while removing excess
    email_to_delete = input().lower().strip()
    
    try:
        contacts = load()
        index_to_delete = None
        email_found = False  # Flag to check if the email is found

        # Goes over list of existing contacts
        for i, contact in enumerate(contacts):
            # Check if email matches
            if contact["email"] == email_to_delete:
                index_to_delete = i
                email_found = True
                break

        if email_found:
            # Remove the contact from the list if found
            deleted_contact = contacts.pop(index_to_delete)
            print(f"Contact deleted: {deleted_contact}")
            print("Deletion successful")
            dump(contacts)
            input('\nPress Enter to Continue...')
        else:
            # Shows when email does not match any from the list
            clear_screen()
            print(f"Value of email: {email_to_delete}")
            print(f"Unable to find contact with email: {email_to_delete}")
            input('\nPress Enter to Continue...')

    except BaseException as be:
        print(f"Error occurred: {be=}, {be}")

    return


# Function to display all existing contact
def show_contacts():
    # Clears terminal screen
    os.system('clear')
    # Displays current menu selection
    header = 'Database Contents'
    print('-' * len(header))
    print(header)
    print('-' * len(header))
    # Loads contact from json
    contacts = load()
    # Lists the loaded contacts
    for n in contacts:
        print(n)
    # Asks for user confirmation before returning back to menu
    print('\nHit ENTER key to continue...')
    input()
    
    
    
