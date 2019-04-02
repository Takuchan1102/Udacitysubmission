import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause("You find yourself in a dark dungeon.")
    print_pause("In front of you are three passageways.")
    print_pause("Which way do you want to go?")


def cave(items):
    print_pause("You have gone astray into the deep cave")
    if "lightsaver" in items:
        print_pause("You cannot find anything more")
    else:
        print_pause("Then...")
        print_pause("You could find out a lightsaver.")
        items.append("lightsaver")
    print_pause("You go back to the original fork in the road.")
    adventure_starwars(items)


def forest(items):
    print_pause("You have gone astray into the deep forest.")
    print_pause("Then...")
    print_pause("You encontered Jedi Master Yoda!!")
    if "force" in items:
        print_pause("Yoda said, 'You already got the force."
                    "There is not anything more to coach you.'")
    else:
        if "lightsaver" in items:
            print_pause("Yoda said,'You are the chosen hero,"
                        "then I can coach you for the force.'")
            print_pause("Now the force is be with you!!")
            items.append("force")
        else:
            print_pause("Yoda said, 'You do not look the chosen"
                        "hero, then I cannot coach you at all '")
    print_pause("You go back to the original fork in the road.")
    adventure_starwars(items)


def volcano(items):
    print_pause("You have reached the summit of volcano finally.")
    print_pause("Then...")
    print_pause("You came across Darth Vader!! Let\'s fight against him ")
    if "lightsaver" in items:
        print_pause("You draw the lightsaver.")
        if "force" in items:
            print_pause("Then you use the force power. Now you"
                        "swing down the lightsaver to Darth Vader!")
            battle = random.randint(1, 2)
            if battle == 1:
                print_pause("You cross lightsaver with Darth Vader.")
                print_pause("But, unfortunately, your lightsaver is broken.")
                print_pause("Darth Vader countered you. You are defeated.")
                gameover(items)
            else:
                print_pause("You finally defeat Darth Vader!!")
                print_pause("You won!! Conglaturations!!!")
                gameover(items)
        else:
            print_pause("You swind down the lightsaver to Darth Vader!!")
            print_pause("Then...")
            print_pause("Wihtout the force, your attack is easily protected.")
            print_pause("Darth Vader countered you. You are defeated.")
            gameover(items)

    else:
        print_pause("You are powerless without a lightsaver.")
        print_pause("Darth Vader attack you. You are defeated.")
        gameover(items)


def adventure_starwars(items):
    print_pause("Please enter the number for the"
                "place you would like to visit.")
    place = input("1. Cave\n"
                  "2. Volcano\n"
                  "3. Forest\n")
    if place == '1':
        cave(items)
    elif place == '2':
        volcano(items)
    elif place == '3':
        forest(items)
    else:
        print("Sorry,it is not correct. Try again.")
        adventure_starwars(items)


def gameover(items):
    response = input("Would you like to play again?(y/n)").lower()
    if response == 'y':
        print_pause("Let\'s continue the adventure again!")
        items = []
        adventure_starwars(items)
    elif response == 'n':
        print_pause("Good bye!")
    else:
        print_pause("Sorry,it is not correct. Try again.")
        gameover(items)


def play_starwars():
    items = []
    intro()
    adventure_starwars(items)

play_starwars()
