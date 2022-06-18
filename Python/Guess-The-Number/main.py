import time
import random


def main():
    lowerBound = int(input("Enter the lower bound: "))
    upperBound = int(input("Enter the upper bound: "))
    tries = 0

    number = random.randint(lowerBound, upperBound)

    print(
        f"Hello. I'm thinking of a number between {lowerBound} and {upperBound}. Can you guess it?")

    guess = int(input("Enter your guess: "))

    while guess != number:
        print("hmmmmm....")
        time.sleep(1)

        if guess > number:
            print("Too high!")
        else:
            print("Too low!")

        tries += 1
        guess = int(input("Enter your guess: "))

    print(
        f"You got it! The number was {number} and it only took you {tries} tries!")

    doYouWannaPlayAgain = input("Do you want to play again? (y/n): ")

    while doYouWannaPlayAgain != "y" and doYouWannaPlayAgain != "n":
        doYouWannaPlayAgain = input("Do you want to play again? (y/n): ")

    if doYouWannaPlayAgain == "y":
        main()
    else:
        print("Goodbye!")
        quit()


if __name__ == "__main__":
    main()
