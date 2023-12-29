# Imports functions from separate python file 
from db_functions import (is_choice_valid, create_new_contact, find_contact, update_contact, delete_contact, show_contacts)
import os
# Imports json file for library read and write
import json


while True:
# Use Case - Main Screen
    # Clears terminal screen
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
            # Calls on to find contact function
            find_contact()
            continue
        # Update existing contact
        elif int_choice == 3:
            os.system("clear")
            print("Update contact was selected")
            print("\nEnter email of contact to update: ")
            # Ask for email for selection
            email = input()
            # Calls on update_contact function and overwrites json file
            update_contact(email)
            continue
        # Delete contact
        elif int_choice == 4:
            print("Delete contact was selected")
            delete_contact()
            continue
        # Displays all the existing contact entries 
        elif int_choice == 5:
            print("Showing Database Contents")
            # Calls on show_contacts function and reads from json file
            show_contacts()
            continue
        # Exits application
        elif int_choice == 6:
            os.system("clear")
            print("Exit was selected; Goodbye!")
            break
    else:
        # Will display if input is invalid and will ask again
        print(f"Invalid choice - {choice}; try again...")
        continue