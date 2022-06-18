import time
import sys


def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)


score = 0

doYouWannaPlay = ""

while len(doYouWannaPlay) == 0:
	doYouWannaPlay = input("Do you want to play this quiz?: ")
	if doYouWannaPlay.lower().strip() == "yes":
		delay_print("Okay let's play!!!")
	elif doYouWannaPlay.lower().strip() == "y":
		delay_print("Okay let's play!!!'")
	if doYouWannaPlay.lower().strip() == "no":
		delay_print("Let's play later then...")
		quit()
	elif doYouWannaPlay.lower().strip() == "n":
		delay_print("Let's play later then...")
		quit()

q1 = ""

while len(q1) == 0:
	q1 = input("\nWhat is Harry's full name?: ")
	if q1.lower().strip() == "harry james potter":
		delay_print("That is correct!!!")
		score += 1
	elif q1.lower().strip() != "harry james potter":
		delay_print("That is not correct.....")

q2 = ""

while len(q2) == 0:
	q2 = input("\nWhat is the final spell that harry casts to finally kill Voldemort?: ")
	if q2.lower().strip() == "expelliarmus":
		delay_print("That is correct!!!")
		score += 1
	elif q2.lower().strip() == "stunning spell":
		delay_print("That is correct!!!")
		score += 1
	else:
		delay_print("That is not correct.....")


print(f"\nYour score is {score}")
