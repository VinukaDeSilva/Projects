import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def main():
    # Rates for each room.
    rates = {
        "single": 4000,
        "double": 6000,
        "family": 8000,
        "standard": 7000,
        "delux": 10000,
        "ramses": 15000
    }

    delay_print("------------------------------------------------------\n")
    delay_print("Welcome to the luxurious Hotel Ramses.\n")
    delay_print("What would you like to do?\n")
    delay_print("A : Book a room.\n")
    delay_print("B : Rent out a suite.\n")
    delay_print("C : Quit.\n")
    delay_print("------------------------------------------------------\n")

    choice_1 = str.lower(input("Your choice : "))
    if choice_1 == "a":
        # Show prices for rooms
        delay_print("--------------------------------\n")
        delay_print("The prices for our rooms are as follows: \n")
        delay_print("Single room : Rs.4000 per night.\n")
        delay_print("Double room : Rs.6000 per night.\n")
        delay_print("Family room : Rs.8000 per night.\n")
        delay_print("--------------------------------\n")

        # Chose and ask for the number of days you are going to spend.
        choice_2 = str.lower(input("Enter your choice : "))
        if choice_2 == "single room":
            delay_print("How many days will you be spending at Hotel Ramses?\n")
            days = int(input("Days : "))

            delay_print("Very well, would you like to proceed to checkout or will you cancel your order?\n")
            choice_3 = str.lower(input("What is your choice (y/n) : "))
            if choice_3 == "y":
                delay_print("Proceeding to checkout...\n")
                time.sleep(0.5)

                delay_print(f"Your price will be Rs.{rates['single'] * days}")
            else:
                delay_print("Cancelling your order...\n")
                time.sleep(2)
                delay_print("We hope to do business in the future with you. Have a nice day...")
                time.sleep(0.5)
        
        elif choice_2 == "double room":
            delay_print("How many days will you be spending at Hotel Ramses?\n")
            days = int(input("Days : "))

            delay_print("Very well, would you like to proceed to checkout or will you cancel your order?\n")
            choice_3 = str.lower(input("What is your choice (y/n) : "))
            if choice_3 == "y":
                delay_print("Proceeding to checkout...\n")
                time.sleep(0.5)

                delay_print(f"Your price will be Rs.{rates['double'] * days}")
            else:
                delay_print("Cancelling your order...\n")
                time.sleep(2)
                delay_print("We hope to do business in the future with you. Have a nice day...")
                time.sleep(0.5)
        
        elif choice_2 == "family room":
            delay_print("How many days will you be spending at Hotel Ramses?\n")
            days = int(input("Days : "))

            delay_print("Very well, would you like to proceed to checkout or will you cancel your order?\n")
            choice_3 = str.lower(input("What is your choice (y/n) : "))
            if choice_3 == "y":
                delay_print("Proceeding to checkout...\n")
                time.sleep(0.5)

                delay_print(f"Your price will be Rs.{rates['family'] * days}")
            else:
                delay_print("Cancelling your order...\n")
                time.sleep(2)
                delay_print("We hope to do business in the future with you. Have a nice day...")
                time.sleep(0.5)

    elif choice_1 == "b":
        # Show the rates for a suite.
        delay_print("--------------------------------\n")
        delay_print("The prices for our suites are as follows: \n")
        delay_print("Standard suite : Rs.7000 per night.\n")
        delay_print("Delux suite : Rs.10000 per night.\n")
        delay_print("Ramses suite : Rs.15000 per night.\n")
        delay_print("--------------------------------\n")

        choice_2 = str.lower(input("Enter your choice : "))
        if choice_2 == "standard suite":
            delay_print("How many days will you be spending at Hotel Ramses?\n")
            days = int(input("Days : "))

            delay_print("Very well, would you like to proceed to checkout or will you cancel your order?\n")
            choice_3 = str.lower(input("What is your choice (y/n) : "))
            if choice_3 == "y":
                delay_print("Proceeding to checkout...\n")
                time.sleep(0.5)

                delay_print(f"Your price will be Rs.{rates['standar'] * days}")
            else:
                delay_print("Cancelling your order...\n")
                time.sleep(2)
                delay_print("We hope to do business in the future with you. Have a nice day...")
                time.sleep(0.5)
        
        elif choice_2 == "delux suite":
            delay_print("How many days will you be spending at Hotel Ramses?\n")
            days = int(input("Days : "))

            delay_print("Very well, would you like to proceed to checkout or will you cancel your order?\n")
            choice_3 = str.lower(input("What is your choice (y/n) : "))
            if choice_3 == "y":
                delay_print("Proceeding to checkout...\n")
                time.sleep(0.5)

                delay_print(f"Your price will be Rs.{rates['delux'] * days}")
            else:
                delay_print("Cancelling your order...\n")
                time.sleep(2)
                delay_print("We hope to do business in the future with you. Have a nice day...")
                time.sleep(0.5)
        
        elif choice_2 == "ramses suite":
            delay_print("How many days will you be spending at Hotel Ramses?\n")
            days = int(input("Days : "))

            delay_print("Very well, would you like to proceed to checkout or will you cancel your order?\n")
            choice_3 = str.lower(input("What is your choice (y/n) : "))
            if choice_3 == "y":
                delay_print("Proceeding to checkout...\n")
                time.sleep(0.5)

                delay_print(f"Your price will be Rs.{rates['ramses'] * days}")
            else:
                delay_print("Cancelling your order...\n")
                time.sleep(2)
                delay_print("We hope you visit again. Have a nice day...\n")
                time.sleep(0.5)

    else:
        delay_print("Exitting program...\n")
        time.sleep(2)
        delay_print("..........\n")


if __name__ == "__main__":
    main()
