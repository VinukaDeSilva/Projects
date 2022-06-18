"""
A University's IT department has 700 students. It is conducting a survey on their job preferences.
Each student uses a computer and inputs their name and chooses one off 5 options:
    1. Software Engineer (Option 1),
    2. Software Architect (Option 2),
    3. System Administrator (Option 3),
    4. Data Analysis (Option 4),
    5. Quality Assurance Analyst (Option 5),
Input the choice of all 700 stdents
Output the names of those who chose Software Engineer
Output the percentage of the students who chose each option.
"""

Count = 1
OneCount = 0
TwoCount = 0
ThreeCount = 0
FourCount = 0
FiveCount = 0
choice = 0
name = ""
OneName = ""

for count in range(1, 701):
    name = input("Enter you name: ")
    choice = int(input(
        "Select an option: 1. Sofware Engineer, 2. Software Architect, 3. System Administrator, 4. Data Analyst, 5. Quality Assurance Analyst"
    ))

    if choice == 1:
        OneName = OneName + "," + name
        OneCount = OneCount + 1
    if choice == 2:
        TwoCount = TwoCount + 1
    if choice == 3:
        ThreeCount = ThreeCount + 1
    if choice == 4:
        FourCount = FourCount + 1
    if choice == 5:
        FiveCount = FiveCount + 1


print("The name of those who chose Software Engineer: ", OneName)
print("The percentage of those who chose Software Engineer: ", OneCount / 700 * 100)
print("The percentage of those who chose Software Architect: ", TwoCount / 700 * 100)
print("The percentage of those who chose System Administrator: ", ThreeCount / 700 * 100)
print("The percentage of those who chose Data Analysis: ", FourCount / 700 * 100)
print("The percentage of those who chose Quality Assurance Analyst: ", FiveCount / 700 * 100)
