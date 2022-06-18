"""Calculator"""


def main():
    while True:
        choice = str.lower(input("Do you want to add, subtract, multiply or divide?: "))
        if choice == "add":
            add()
        elif choice == "subtract":
            subtract()
        elif choice == "multiply":
            multiply()
        elif choice == "divide":
            divide()
        else:
            print("Invalid input")

        exit = str.lower(input("Do you want to exit? (y/n): "))
        if exit == "y":
            break
        else:
            continue


def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")


def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"{num1} - {num2} = {num1 - num2}")


def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"{num1} * {num2} = {num1 * num2}")


def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"{num1} / {num2} = {num1 / num2}")


if __name__ == "__main__":
    main()
