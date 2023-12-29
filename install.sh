#!/bin/bash

# *** Installation Process ***
# step 1: check if python3 is installed on local machine
if command -v python3 &> /dev/null; then
    echo "Python3 is present in the environment"
else
    if
        command -v apt-get &> /dev/null; then
        echo "Will attempt to install Python3 via apt-get..."
        sudo apt-get update && apt-get install -y python3
    else
        echo "Ooops: I'm unable to install Python3."
        echo "Please make sure you have the permission to run apt-get"
        exit 1
    fi
fi

# step 2: check if python3 was installed successfully
if command -v python3 &> /dev/null; then
    echo "We're good to proceed with installation..."
else
    echo "Python3 is either not installed or could not be installed. Please check with your administrator."
    exit 1
fi

# step 3: create a folder that will contain the Python program and the json db file
#!/bin/bash

# Check if the "app" folder already exists
if [ -d "app" ]; then
    echo "The 'app' folder already exists - deleting the old app folder."
else
    # Create the "app" folder
    mkdir app
    echo "The 'app' folder has been created in the current directory."
fi

# step 4: move the program file and the json db file into the app folder
cp user_database.py db_functions.py simple_db.json ./app

# step 5: make the application script executable for the current user
cd app
chmod u+x user_database.py

echo "Done."
echo
echo "The application has been installed inside the app folder."
echo 
echo "Use the following syntax to run the application:"
echo
echo "$ ./user_database.py"



