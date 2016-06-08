from sys import exit
import tkMessageBox
import random
import copy


# global variables
inventory = []
has_picked_fruit = False
has_picked_weapon = False
has_picked_song = False
work_or_not = False
boss_happy = False
has_played_with_police = False
extra_list = []
a = ["Huh?", "What?", "Uhm.", "Don't get it.", "Be specific man.", "Rofl. U funny man."]
has_picked_country = False


def start():
    print "Hello there! What is your name?"

    name = raw_input("Please type your name: ")

    print "Welcome, %s." % name
    adventuretime()


def adventuretime():
    print "Today we're going on an adventure."
    print "\nAre you up for the thrill?!"

    thrill = raw_input("> Please type \"yes\" or \"no\": ")
    thrill = thrill.lower().strip()

    if thrill == "yes":
        inventory_fruit()
    elif thrill in ("ok", "okay", "yo"):
        inventory_fruit
    elif thrill == "no":
        exit("You're boring like a bag of potatoes. You basic b&&&h.")
    else:
        print "\nI have no idea what that means, but you will get excited along the way."
        inventory_fruit()


def inventory_fruit():
    global has_picked_fruit
    global to_be_eaten
    print "\nYou are going to build an inventory."
    print "Pick one of the following fruits to add to your inventory:"
    print "\nBanana, pear, apple, pineapple."

    while not has_picked_fruit:
        fruit = raw_input("--> Pick your fruit: ")
        fruit = fruit.lower().strip() # normalize the input

        to_be_eaten = copy.copy(fruit) # USE OUTSIDE FUNCTION POSSIBLE?
        extra_list.append(to_be_eaten)

        for option in ('banana', 'pear', 'apple', 'pineapple'):
            if option in fruit:
                inventory.append(option)


        if len(inventory) > 0:
            has_picked_fruit = True
            print "Your inventory now holds: %s" % inventory
            inventory_weapon()

        else:
            print "Sorry, only these fruits are available."

def inventory_weapon():
    global has_picked_weapon
    print "\nNow you will pick a weapon too."
    print "You can choose one of the following:"
    print "\nGun, taser, rock, paperclip."

    while not has_picked_weapon:
        weapon = raw_input("--> Pick your weapon: ")
        weapon = weapon.lower().strip() # normalize the input

        if weapon in ("gun", "taser", "rock", "paperclip"):
            inventory.append(weapon)
            print "Your inventory now holds the following items: %s" % inventory
            has_picked_weapon = True
            inventory_song()
        else:
            print "No, stop getting jolly, you can pick one of the above only."

def inventory_song():
    global has_picked_song
    print "\nLastly, you can pick some tunes from a cool artist."
    print "Are you a Belieber?"

    while not has_picked_song:
        song = raw_input("yes/no: ")
        song = song.lower().strip()

        if song == "yes":
            inventory.append("Justin Bieber")
            print "\nCongratulations, you picked Justin Bieber."
            print "Your whole inventory now consists of: %s" % inventory
            has_picked_song = True
            worktime()
        elif song in ("no", "nope"):
            print "\nYou don't like Justin? Then you get Lil' Wayne.",
            print "Get crunk y'all."
            inventory.append("Lil' Wayne")
            print "Your whole inventory now consists of: %s" % inventory
            has_picked_song = True
            worktime()
        else:
            print "Sorry, iTunes is broken. Just these two is what you get."
            print "So, Justin, yes or no?"


def worktime():
    global work_or_not
    print "\nYou have a job. Today you have to work. Do you want to go?"

    while not work_or_not:
        want_work = raw_input("> yes/no: ")

        if want_work in ("yes", "yea", "yap"):
            work_or_not = True
            angry_boss()

        elif want_work in ("nope", "no", "nah"):
            work_or_not = True
            walk_park()
        else:
            print "It's a simple yes or no question."


def angry_boss():
    global boss_happy
    print "\nAs soon as you step into the office, your boss starts screaming at you."
    print "You have no idea what's up. Major raging going on."
    print "You get annoyed."

    while not boss_happy:
        boss_games = raw_input("\n> You can either shout, curse, call the boss names, scream, run away.. Oh the boss likes cookies too!: ")
        boss_games = boss_games.lower().strip() # normalize the input

        if ('shout' in boss_games) or ('curse' in boss_games) or ('call' in boss_games) or ('asshole' in boss_games):
            print "\nHe/she heard that."
            print "Chairs and stools are being thrown through the office."
            print "In your direction. Better watch your head."
            print """
            Now your computer got pulled out of the sucket, and
            chucked towards your head. You are starting to get scared.

            """
            print "\n\n.... AAAAAAAAAAAAAAAAAAAAAHHHHHH!!!!!"
            print "\nYou scream and run away."
            boss_happy = True
            work_escalation()

        elif ('scream' in boss_games) or ('run' in boss_games):
            print "So you choose to scream and run away."
            print "\n\n.... AAAAAAAAAAAAAAAAAAAAAHHHHHH!!!!!"
            print "\nPussy."
            boss_happy = True
            work_escalation()

        elif boss_games == "give cookie":
            print "\nYour boss is happy."
            print "He/she gives you a raise. And a smiley face sticker."
            print "You even get granted a vacation."
            boss_happy = True
            travel_time()

        else:
            dead("You accidentally fall of the roof of your office building and die.")


def prison_time():
    tkMessageBox.showinfo(title="Prison partytime biatches", message="You are in a cell. And you are not alone. You are not having fun :(")
    dead("You get raped there so many times, that your own butthole eats you up. There is no saving possible.")

def work_escalation():
    print """
    \nTHIS SHETT IS OUTTA CONTROL.
    You fear for your life. This means there are only two options.
    1. We HAVE to call the police. They'll take care of the situation.
    2. Set the office building on FIRE.
    """

    fire_building = raw_input("> Choose 1/2: ")

    if fire_building == "1":
        print "\nUh oh. They are corrupt. Your boss pays them."
        print "Instead, you get to spend time in jail."

        prison_time()

    elif fire_building == "2":
        print "\nYou're such an enlighter. Due to a broken fire alarm system",
        print "No one gets a chance to escape. Every burns."
        print "Not only your boss. Little fireball."

        fire_time()



def fire_time():
    global inventory
    global has_played_with_police
    print "\nUh oh! Due to burning down a building, you are sought after by the police."
    print "This is where your inventory comes in handy!"
    print "\nYour inventory consists of: %s" % inventory
    attack_the_police_with = random.choice(inventory)

    print "\nYou used %s to attack zhe police." % attack_the_police_with
    print "Dammit, that didn't work."
    print "\nYour inventory consists of: %s" % inventory

    while not has_played_with_police:
        weapon_fetched_from_inventory = raw_input("Pick the weapon: ")
        weapon_fetched_from_inventory = weapon_fetched_from_inventory.lower().strip() # normalize the input

        if weapon_fetched_from_inventory == "gun":
            print "\nHold it like a bazooka in Arnold Schwarzenegger style."
            print "BENG BENG. Major massacre."
            has_played_with_police = True
            army_time()
        elif weapon_fetched_from_inventory == "taser":
            print "\nBZZZ BZZ."
            print "This is fun! A dude hits the floor all shaking. But wait, oh no! The taser blocks."
            has_played_with_police = True
            dead("\nYour body gets blown to pieces by rifle fires. Whoops.")
        elif weapon_fetched_from_inventory == "rock":
            print "\nYou pick up the rock and smash in the head of the dude closest to you."
            has_played_with_police = True
            army_time()
        elif weapon_fetched_from_inventory == "paperclip":
            print "\nWith an elastic band you find on the streets, you make a katapult."
            print "You pick up some junk on the floor and katapult it to the enemy."
            print "It does not help."
            has_played_with_police = True
            army_time()
        else:
            print "DUDE PICK YOUR WEAPON, YOU ARE UNDER ATTACK!"




def army_time():
    global extra_list
    global has_picked_country
    global a

    print "\nWhat a show. In the meantime, you eat your %s. Hmmmm jummie!" % extra_list[0]
    print "Uh oh, you kill all the police. New police dudes are sent. You kill those too."
    print "\n\nBecause you are a sadistic maniac killer, the army is now after you."
    print "Instead of fighting the army like a man, you flee the country."
    print "Mexico, Cuba or Colombia sounds nice."

    while not has_picked_country:

        escape_country = raw_input("\n>Pick Mexico, Cuba or Colombia: ")
        escape_country = escape_country.lower().strip() # normalize the input

        if escape_country == "mexico":
            has_picked_country = True
            dead("You get mugged and taken as a hostage as soon as you hit the ground. You never see daylight again.")
        elif escape_country == "cuba":
            print "You spend the rest of your life smoking fine cigars. You enjoy them. The end."
            has_picked_country = True
            exit(0)
        elif escape_country == "colombia":
            print "You get mugged after seemingly friendly strangers swipe your face with scolapamine."
            has_picked_country = True
            dead("Days later you wake up naked in a cottage miles away from any city.")
        else:
            print random.choice(a)


def walk_park():
    print "There's a lost dog. You go walk with it to think about life."
    print "You reach a serene state of mind and are grateful for what you have."
    exit(0)


def travel_time():
    print "You're gonna go on trip. Going on a trip. Going on a trip."
    print "Plus, you get a lifetime supply of cookies! Just to share the lovin'."
    print "\nYou get sent to Costa Rica. Because you're a nerd, you want to practice coding whilst on vacation."
    print "Good luck with the next exercises!"
    exit(0)



def dead(why):
    print why, "Good job!"
    exit(0)


if __name__ == '__main__':
	start()
