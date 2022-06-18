import random
import time

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$%#"

while True:
    password_len = int(input("How long would you like your password to be: "))
    password_count = int(input("How many passwords would you like: "))

    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_character = random.choice(characters)
            password += password_character
        print(f"Your newly created password is {password}")

    do_u_wanna_continue = input("Do you want to repeat this function(y/n): ")
    if do_u_wanna_continue != "y":
        print("Exiting programme........")
        time.sleep(1)
        print("You left")
        quit()
    else:
        continue
