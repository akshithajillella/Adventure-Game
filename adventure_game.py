import time
import random


def print_pause(message, sleep_time=2):
    print(message)
    time.sleep(sleep_time)


def intro(item):
    creatures = ['troll', 'pirate', 'wicked fairie', 'gorgon']
    enemy = random.choice(creatures)
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")
    field(item, enemy)


def field(item, enemy):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice = input("(Please enter 1 or 2.)\n")
        if choice == '1':
            house(item, enemy)
            break
        elif choice == '2':
            cave(item, enemy)
            break


def house(item, enemy):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if 'sword' not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    while True:
        choice = input("Would you like to (1) fight or (2) run away?")
        if choice == '1':
            if 'sword' not in item:
                print_pause("You do your best...")
                print_pause(f"but your dagger is no match for the {enemy}.")
                print_pause("You have been defeated!")
                play_again()
                break
            else:
                print_pause(f"As the {enemy} moves to attack, you unsheath "
                            "your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in your "
                            "hand as you brace yourself for the attack.")
                print_pause(f"But the {enemy} takes one look at your "
                            "shiny new toy and runs away!")
                print_pause(f"You have rid the town of the {enemy}. "
                            "You are victorious!")
                play_again()
                break
        elif choice == '2':
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been followed.")
            field(item, enemy)
            break


def cave(item, enemy):
    print_pause("You peer cautiously into the cave.")
    if 'sword' not in item:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.")
        item.append("sword")
        field(item, enemy)
    else:
        print_pause("You've been here before, "
                    "and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field(item, enemy)


def play_again():
    item = []
    while True:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'y':
            print_pause("Excellent! Restarting the game ...")
            intro(item)
            break
        elif choice == 'n':
            print_pause("Thanks for playing! See you next time.")
            break


def play_game():
    item = []
    intro(item)


play_game()
