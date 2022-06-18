import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Quiz:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

        q = input(f"{self.question}: ").lower().strip()

        if q == self.answer:
            delay_print("Correct!!!")
        else:
            delay_print(f"Incorrect, the correct answer is '{self.answer}'.")
    
    def do_or_do_not(self):
        do = input("Do you wish to continue?: ")

        if do == 


q1 = Quiz("How old was Harry Potter when he 'died'?", "17".title())
q2 = Quiz("\nHow old was Albus Dumbledore when he died?", "115".title())
q3 = Quiz("\nHow old was James Potter when he died?", "21".title())
q4 = Quiz("\nWhat is Lord Voldemort's real name?", "tom marvolo riddle".title())
q5 = Quiz("\nHarry Potter is a descendant of which Peverell?", "ignotus peverell".title())
q6 = Quiz("\nBefore arriving in Godric's Hollow, where did the dumbledore family live?", "mould on the wold".title())

time.sleep(5)
