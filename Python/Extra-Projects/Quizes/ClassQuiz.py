# Create a quiz using a class
import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")


class Quiz:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def create(self):
        q = input(f"{self.question}: ").lower().strip()
        if q == self.answer:
            delay_print("That is correct!")
        else:
            delay_print("That is incorrect.")


q1 = Quiz("What is Harry Potter's full name?", "harry james potter").create()
q2 = Quiz("What wood is Draco Malfoy's wand made of?", "blackthorn").create()
q3 = Quiz("In the final book, who does Hermione turn into when using the Polyjuice potion?", "bellatrix lestrange").create()
q4 = Quiz("Who does Harry Potter marry?", "ginny weasley").create()
q5 = Quiz("What is the name of the creature that lived in the Chamber of Secrets?", "basilisk").create()
