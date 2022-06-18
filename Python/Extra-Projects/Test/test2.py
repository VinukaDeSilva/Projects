"""
A small cafe sells 05 types of items:
    bun - $0.50
    coffee - $1.20
    cake - $1.50
    sandwich - $2.10
    dessert - $4.00

Write a programme that inputs every item sold during that day.

The programme:
    Uses an item called 'end' to finish the day's input.
    Adds up the daily amount taken for each type of item.
    Output the total takings (For all the items added together) at the end of the day.
    Output the type of item taken that has the highest takings at the end of the day.
"""

NumBun = 0
NumCoffee = 0
NumCake = 0
NumSandwich = 0
NumDessert = 0
BunPrice = 0
CoffeePrice = 0
CakePrice = 0
SandwichPrice = 0
DessertPrice = 0

name = input("Enter the product name. Type 'end' to exit the programme.")

while name != "end":
    if name == "bun":
        NumBun += 1
        BunPrice += 0.50
    elif name == "coffee":
        NumCoffee += 1
        CoffeePrice += 1.20
    elif name == "cake":
        NumCake += 1
        CakePrice += 1.50
    elif name == "sandwich":
        NumSandwich += 1
        SandwichPrice += 2.10
    elif name == "dessert":
        NumDessert += 1
        DessertPrice += 4.00
    else:
        print("Invalid product name.")

    name = input("Enter the product name. Type 'end' to exit the programme.")

# Find the product with the highest number of takings
if NumBun > NumCoffee and NumBun > NumCake and NumBun > NumSandwich and NumBun > NumDessert:
    highestProduct = "bun"
    highestNum = NumBun
    highestPrice = BunPrice
elif NumCoffee > NumBun and NumCoffee > NumCake and NumCoffee > NumSandwich and NumCoffee > NumDessert:
    highestProduct = "coffee"
    highestNum = NumCoffee
    highestPrice = CoffeePrice
elif NumCake > NumBun and NumCake > NumCoffee and NumCake > NumSandwich and NumCake > NumDessert:
    highestProduct = "cake"
    highestNum = NumCake
    highestPrice = CakePrice
elif NumSandwich > NumBun and NumSandwich > NumCoffee and NumSandwich > NumCake and NumSandwich > NumDessert:
    highestProduct = "sandwich"
    highestNum = NumSandwich
    highestPrice = SandwichPrice
elif NumDessert > NumBun and NumDessert > NumCoffee and NumDessert > NumCake and NumDessert > NumSandwich:
    highestProduct = "dessert"
    highestNum = NumDessert
    highestPrice = DessertPrice

totalNum = NumBun + NumCoffee + NumCake + NumSandwich + NumDessert
totalPrice = BunPrice + CoffeePrice + CakePrice + SandwichPrice + DessertPrice

print(f"{NumBun} buns were sold, generating a revenue of {BunPrice} from buns.")
print(f"{NumCoffee} coffees were sold, generating a revenue of {CoffeePrice} from coffees.")
print(f"{NumCake} cakes were sold, generating a revenue of {CakePrice} from cakes.")
print(f"{NumSandwich} sandwiches were sold, generating a revenue of {SandwichPrice} from sandwiches.")
print(f"{NumDessert} desserts were sold, generating a revenue of {DessertPrice} from desserts.")

print(
    f"The total number of items sold was {totalNum}, generating a total revenue of {totalPrice} for the day.")

print(
    f"The product that was sold the most was {highestProduct}, with {highestNum} items sold, generating a revenue of {highestPrice}.")
