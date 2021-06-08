# Files
# Hacking The Spider (computer hacker)
# Work with Python files to  retrieve, manipulate, obscure, and create data.
# work with CSV files and other text files.

# Problem
# The Spider, a computer hacker, has compromised several top-secret passwords.

# passwords.csv
# Username,Password
# jean49,Da*E%OuGuc9$V1m
# haydenashley,l$r^9eGg8f@BZhy
# michaelastephens,$1sp++bga8H+eCr
# denisephillips,Vj)T7AsfRHkfpvw
# andrew24,T^mH8LMM&0C3VVk
# kaylaabbott,!nN05pv3tc(DBO(
# tmartinez,V46_Xx85_gKg7rt
# mholden,(sd44x3x*A7D1dA
# randygilbert,A7+E0YfB+MLPJ8Z
# watsonlouis,i!4(DEkBLNq)C7G
# mdavis,c$2VXHnxQ+6ifpx
# patrickprice,Es_r0GlF&zDkJKG
# kgriffith,%0dUpqgwFfA$Dma
# hannasarah,c(9au%x)tyC#HDd
# xaviermartin,e7!gWemxlde3K6p
# hrodriguez,od@9P!dfQj8NH&A
# erodriguez,hB+4A(si*vdHl4c
# danielleclark,2lv3HKAs+Or8R48
# timothy26,oz7ExOUI2&*S87h
# elizabeth19,x3C8yYtI!(e3+z(

# Mission
# 1. acquire access to The Spider's systems and read compromised usernames and passwords stored in a file called "passwords.csv"
# 2. update The Spider's "passwords.csv" file to scramble the secret data.
# 3. add the signature of Glow Worm, a different hacker who could be halted by The Spider if they viewed Glow Worm as a threat.

# Mission 1
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
  
# Mission 3
# Hide trail and pin rival hacker, Glow Worm as person behind this attack. Add Glow Worm's signature:-
  glow_worm_sig = """
  
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/  

  ___ 
 / __)
( (_ \(
 \___/

____    ____
(  )     ( )
/ (_/\/\_) \
\____/\____/


"""

# Write glow_worm_sig to new_passwords_obj. Now we have the file to replace passwords.csv with
  new_passwords_obj.write(glow_worm_sig)
# output
# new_password.csv file is created (and content is:- you got hacked gw)

