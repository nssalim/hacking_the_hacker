# Files
# Hacking The Spider (computer hacker)
# Work with Python files to  retrieve, manipulate, obscure, and create data.
# work with CSV files and other text files.

# Problem
# The Spider, a computer hacker, has compromised several top-secret passwords.

# Mission
# 1. acquire access to The Spider's systems
# 2.  update The Spider's "passwords.txt" file to scramble the secret data.
# 3.  add the signature of Glow Worm, a different hacker who could be halted by The Spider if they viewed Glow Worm as a threat.


# Mission 1 - 
# Reading In The Passwords
# Write a program able to read compromised usernames and passwords stored in a file called "passwords.csv" on The Spider's machine.
import csv
import json

compromised_users = []
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    # print(password_row['Username'])
# output
# list of usernames (of each person whose password was compromised)

# Add each username to the list of compromised_users.
    compromised_users.append(password_row['Username'])
    # print(compromised_users)
# output
# add username (of each person whose password was compromised) to list of compromised_users.

# Write the username of each compromised_user in compromised_users to compromised_user_file
with open ('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)
# output
# compromised_users.txt file is created (and contains username of each compromise user)


# Notify the Boss
# advise success in retrieving compromised data.
# use JSON to encode said message over the internet.

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
  "recipient":"The Boss", 
  "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)
# output
# boss_message.json file is created (and content is:- 
# {"recipient": "The Boss", 
# "message": "Mission Success"})

# Mission 2
# Scrambling the Password
# after safely recovering the compromised users, completely remove the "passwords.csv" file.
with open("new_passwords.csv", "w") as new_passwords_obj:
    