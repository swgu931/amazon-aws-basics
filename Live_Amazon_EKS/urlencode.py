import sys
import urllib.parse

print("################################")
print("## Welcome to the Lab Encoder ##")
print("################################")

print()
password = input("Enter your Git Password: ")
input("Thank you. Press ENTER to URL encode your Git Credentials")

encodedPassword = urllib.parse.quote(password, safe='')

print()
print("This is your urlencoded Password: ", encodedPassword)sh-4.2$ 
