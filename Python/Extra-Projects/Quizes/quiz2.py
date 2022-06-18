import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


questions = ["What is the capital of France?", "How much did Elon Musk value Twitter at?", "When was the first Star Wars film released? (year is sufficient)"]
answers = ["paris", "43 million", "1977"]


def main():

    delay_print("Welcome to the quiz!\n")
    delay_print("You will be asked a series of questions.\n")
    delay_print("You have 3 lives.\n")
    delay_print("If you get a question wrong, you will lose a life.\n")
    delay_print("If you were to lose all 3 lives, you will lose.\n")
    delay_print("Note: Once you start the quiz, you will have to continue the quiz till it ends or till you lose.\n")
    delay_print("Good Luck!\n")
    print("\n")

    lives = 3
    questionTotal = len(questions)
    answerNo = 0
    score = 0

    if lives > 0:
        for question in questions:
            print(question)
            answer = input("Answer: ")
            if str.lower(answer) == answers[answerNo]:
                delay_print("Correct!\n")
                score += 1
            else:
                delay_print("Wrong!\n")
                lives -= 1
                delay_print("You have " + str(lives) + " lives left.\n")
            answerNo += 1
    else:
        delay_print("You lost!\n")

    delay_print(f"You ended up with a score of {score} out of {questionTotal}.")


if __name__ == "__main__":
    main()
