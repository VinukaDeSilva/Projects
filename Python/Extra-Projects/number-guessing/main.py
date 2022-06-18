# Import the random module
import random


# Create a number gussing game
def main():
    print("You have 5 tries to guess a number between 1 and 10")
    N = 10 
    tries = 0
    n = random.randint(1, N) 
    guesses = 0
    while guesses < 5:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == n:
            print("You got it!")
            break
        elif guess < n:
            print("Too low!")
            tries += 1
        elif guess > n:
            print("Too high!")
            tries += 1

        guesses += 1


    # Print the number of guesses
    print(f"You guessed it in {tries+1} tries!")

if __name__ == "__main__": 
    main()