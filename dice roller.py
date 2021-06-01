import random

while True:
 print(f"The value is ", random.randint(1,6))

 print ("Do you want to rll the dice again")
 choice = input("Enter y for yes or n for no: ")

 if choice == "n":
    break
