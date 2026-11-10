#!/usr/bin/env python
# Author: Mekan Bayramov
# Date: october  23, 2026
# This program checks the username and gives access.
username = input("Login: >> ") # Ask the user to enter a username.
user1 = "Jack" # Save the first username.
user2 = "Jill" # Save the second username.
if username == user1: # Check if the username is Jack.
    print("Access granted")  # Give access to Jack.
elif username == user2: # Check if the username is Jill.
    print("Welcome to the system")     # Welcome Jill.
else: # If the username is not Jack or Jill.
    print("Access denied")  # Do not give access.
