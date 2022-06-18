# Simple battle simulator in the style of Pokemon.
# author: Prendy, edited by: Vinuka De Silva
# [Vinuka] This is not my own creation. I found this on the internet and changed and fixed the code here and there

import random

moves = {"basic move": range(18, 26),
         "special move": range(10, 36),
         "heal": range(10, 20)}


class Character:
    """ Define our general Character which we base our player and Opponent off """
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player(Character):
    """ The player, they start with 100 health and have the choice of three moves """
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        while True:
            choice = str.lower(input("\nWhat move would you like to make? (basic move, special move, or Heal): "))

            if choice == "heal":
                self.health += int(random.choice(moves[choice]))
                print(f"\nYour health is now {self.health}.")
                break
            if choice == "basic move" or choice == "special move":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print(f"\nYou attack with {choice}, dealing {damage} damage.")
                break
            else:
                print("Not a valid move, try again!")


class Opponent(Character):
    """ The Opponent, also starts with 100 health and chooses moves at random """
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        if self.health <= 35:
            # increasing probability of heal when under 35 health, bit janky
            moves_1 = ["basic move", "special move", "heal", "heal", "heal", "heal", "heal"]
            Opponent_choice = random.choice(moves_1)
        else:
            Opponent_choice = random.choice(list(moves))
        if Opponent_choice == "basic move" or Opponent_choice == "special move":
            damage = int(random.choice(moves[Opponent_choice]))
            other.health -= damage
            print(f"\nThe Opponent attacks with {Opponent_choice}, dealing {damage} damage.")
        if Opponent_choice == "heal":
            self.health += int(random.choice(moves[Opponent_choice]))
            print(f"\nThe Opponent uses heal and its health is now {self.health}.")


def battle(player, Opponent):
    print("An enemy Opponent enters...")
    while player.health > 0 and Opponent.health > 0:
        player.attack(Opponent)
        if Opponent.health <= 0:
            break
        print(f"\nThe health of the Opponent is now {Opponent.health}.")
        Opponent.attack(player)
        if player.health <= 0:
            break
        print(f"\nYour health is now {player.health}.")
    # outcome
    if player.health > 0:
        print("You defeated the Opponent!")
    if Opponent.health > 0:
        print("You were defeated by the Opponent!")

if __name__ == '__main__':
    battle(Player(), Opponent())
