import os
import json


# Checks if input choice is valid
def is_choice_valid(arg):
    try:
        int_val = int(arg)
        # Sets the range for menu selection
        if 1 <= int_val <= 6:
            return True
        return False 
    except ValueError as ve:
        return False
    except BaseException as be:
        return False


# Function for creating new contact
def create_new_contact():
    header = "Adding New Contact"
    print("-" * len(header))
    print(header)
    print("-" * len(header), "\n")
    print("Enter First Name: ")
    first_name = input()
    print("Enter Last Name: ")
    last_name = input()
    print("Enter Mobile Number: ")
    mobile = input()
    print("Enter Email Address: ")
    email = input()


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

while True:
    choice = input()
    if is_choice_valid(choice):
        int_choice = int(choice)
        # Create new contact
        if int_choice == 1:
            print("Create contact was selected")
            pass
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