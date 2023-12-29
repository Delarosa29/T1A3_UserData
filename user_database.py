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
    

# Use Case - Main Screen
os.system("clear")
header = "Simple Database"
print("-" * len(header))
print(header)
print("-" * len(header), "\n")

print("1. Create new contact")
print("2. Retrieve a contact by email")
print("3. Update a contact by email")
print("4. Delete a contact by email")
print("5. Show Database Contents")
print("6. Exit\n")