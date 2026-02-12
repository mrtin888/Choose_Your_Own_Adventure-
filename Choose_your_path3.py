# ===============================
# DECISION ADVENTURE GAME - EXPANDED VERSION
# ===============================

# This function shows the introduction of the game
def intro():
    print("=== THE FALL OF THE TYRANT ===\n")
    print("In this world, power is taken with blood.")
    print("Your village was burned.")
    print("Your family was slaughtered.")
    print("Only you survived.\n")

    # input() allows the user to type something
    # .lower() converts text to lowercase so "Yes", "YES", "yes" all work
    choice = input("Do you seek revenge? (yes/no): ").lower()
    return choice


# This function lets the player choose a weapon
def choose_weapon():
    print("\nBefore your journey begins, choose your weapon.")
    weapon = input("Choose (sword/bow): ").lower()
    return weapon


# Sword path function
# Notice we pass variables inside the parentheses (name, health, reputation)
# That means we are sending those values into the function
def sword_path(name, health, reputation):

    print(f"\n{name}, you chose the sword.")  
    # f"" is called an f-string
    # It allows us to insert variables inside the string using { }
    # So {name} becomes whatever the player typed

    print("Steel reflects your burning desire for vengeance.")
    print("You walk into the forest where the Tyrant's squire hunts peasants.\n")

    action = input("Do you attack directly or intimidate him? (attack/intimidate): ").lower()

    if action == "attack":
        print("\nYou charge forward without fear.")
        print("The clash of steel echoes through the trees.")

        health -= 30   # -= means health = health - 30
        reputation += 10

        print("You defeat him but suffer injuries.")
        print(f"Health remaining: {health}")
        print(f"Reputation increased to: {reputation}")

    elif action == "intimidate":
        print("\nYou speak of his inevitable death.")
        print("Fear consumes him. He flees.")
        reputation += 20

        print(f"Reputation increased to: {reputation}")

    else:
        print("You hesitated. Opportunity lost.")

    return health, reputation  # We return updated values


# Bow path
def bow_path(name, health, reputation):

    print(f"\n{name}, you chose the bow.")
    print("From distance comes control.")
    print("From patience comes victory.\n")

    action = input("Do you shoot from distance or follow silently? (shoot/follow): ").lower()

    if action == "shoot":
        print("\nYour arrow flies through the air.")
        print("It pierces his chest.")
        reputation += 15

    elif action == "follow":
        print("\nYou follow him quietly.")
        print("He leads you to the Tyrant's fortress.")
        reputation += 25

    else:
        print("You lost your chance.")

    return health, reputation


# Final confrontation
def final_battle(name, health, reputation):

    print("\n=== THE FINAL CONFRONTATION ===")
    print("You stand before the gates of the Tyrant's fortress.")
    print("Smoke rises from distant villages.")
    print("This ends tonight.\n")

    # The outcome will depend on health and reputation
    if health > 50 and reputation >= 20:
        print("Villagers join your cause.")
        print("Together, you storm the fortress.")
        print(f"{name} defeats the Tyrant in honorable combat.")
        print("ENDING: The Liberator")

    elif health > 20:
        print("You fight alone.")
        print("The duel is brutal.")
        print("You kill the Tyrant… but collapse from wounds.")
        print("ENDING: The Broken Avenger")

    else:
        print("You are too weak.")
        print("The Tyrant overpowers you.")
        print("Your vengeance dies with you.")
        print("ENDING: The Fallen")


# Main function - this controls the whole game
def main():

    # Initial stats
    health = 100
    reputation = 0

    start = intro()

    if start == "yes":

        name = input("\nWhat is your name, warrior? ")

        print(f"\n{name}, your path is now set.")

        weapon = choose_weapon()

        if weapon == "sword":
            health, reputation = sword_path(name, health, reputation)

        elif weapon == "bow":
            health, reputation = bow_path(name, health, reputation)

        else:
            print("You failed to choose a weapon.")
            return  # stops the function early

        final_battle(name, health, reputation)

    else:
        print("Revenge is a fools game.")


# This line starts the program
main()
