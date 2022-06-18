# Enter the player's name
name = input("What is your name?: ")
print(f"Hello {name}")

# Scoring system
score = 0
totalScore = 2

# Ask if the user wants to play the game
WouldYouLikeToPlay = input("Would you like to play this game? (y/n): ")
if WouldYouLikeToPlay == "y":
    print("Let's get started then....")

    # The first question
    Q1 = input("Question 1: What is the full name of the main protagonist of the Harry Potter series?: ")
    if Q1.lower() == "harry james potter":
        print("That is correct!")
    else:
        print("That is wrong!")
    
    # The second question
    Q2 = input("Question 2: What is the total of 21 and 34?: ")
    if Q2 == "55":
        print("That is correct!")
    else:
        print("That is wrong!")
    
    
    print(f"The total score that you have accumulated is {score} out of {totalScore}, {name}. Hope you enjoyed this game. Goodbye....")
else:
    print("Let's play later then....")
