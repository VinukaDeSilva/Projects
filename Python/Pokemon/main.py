import random

moves = {
    "basic move": range(15, 25),
    "special move": range(12, 32),
    "heal": range(8, 22)
}


class Character:
    """We create the Character class that we use to represent the player and their opponent"""

    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError()


class Player(Character):
    # The player starts with 100 health
    def __init__(self, health=100):
        super().__init__(health)

    # Set an attack function that gives the player 3 moves
    def attack(self, other):
        while True:
            choice = str.lower(
                input("What move woulf you like to chose:  basic move, special move, heal: "))

            if choice == "basic move" or choice == "special move":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print(f"You attach with {choice}. You dealt {damage} damage")
                break
            elif choice == "heal":
                self.health += random.choice(moves[choice])
                print(f"Your health is now {self.health}.")
                break
            else:
                print("Not a valid move. Try again.")


class Opponent(Character):
    # The opponent starts with 100 health
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        # Increasing probability to heal if health is less than 35
        if self.health < 35:
            moves_1 = ["basic move", "special move", "heal", "heal", "heal"]
            Opponent_choice = random.choice(moves_1)
        else:
            Opponent_choice = random.choice(list[moves])

        if Opponent_choice == "basic move" or Opponent_choice == "special move":
            damage = int(random.choice(moves[Opponent_choice]))
            other.health -= damage
            print(
                f"Opponent attack with {Opponent_choice}. He dealt {damage} damage")
        elif Opponent_choice == "heal":
            self.health += random.choice(moves[Opponent_choice])
            print(f"Opponent's health is now {self.health}.")


def battle(player, Opponent):
    print("Enemy opponent enters...")

    while player.health > 0 and Opponent.health > 0:
        player.attack(Opponent)
        if Opponent.health <= 0:
            break
        print(f"Opponent's health is now {Opponent.health}")
        Opponent.attack(player)
        if player.health <= 0:
            break
        print(f"Your health is now {player.health}.")

    if player.health > 0:
        print("You defeated the opponent!")
    if Opponent.health > 0:
        print("You were defeated by the opponent!")


if __name__ == "__main__":
    battle(Player(), Opponent())
