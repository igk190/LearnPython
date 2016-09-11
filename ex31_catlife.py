import time

## start game ##

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print color.BOLD + 'Hello World !' + color.END


intro = ["\n", "\n" ,"W E L C O M E", "\n", "T O", "\n", "C A T L I F E", "\n", "\n"]

for word in intro:
	print word
	time.sleep(.2)

print "\nYou are a cat. You are cute and fluffy. What is your name?"

name = raw_input("\n\nPlease fill out name: ")
time.sleep(.1)

print "\nAll right, %s! Let's start the day." % name
time.sleep(.3)

def cat_newlife():
	print "\nYou are grateful. The sun is shining."
	print "There's my human. You jump on the owners lap. Good job!"
	time.sleep(0.5)
	print "\n******* The end ******."

def catmilk_dead():
	print "OH NOOOOOO. You drank it again! You silly kitty."
	print color.BOLD + "Bacteries swarm through your belly." + color.END
	print "You die :( "
	time.sleep(0.8)
	print("\n\nYou are a cat. You have nine lives. You've used one. There are 8 left.")
	cat_newlife()

def cat_sleep():
	print "\nNap time! There's the dogs basket."
	time.sleep(0.5)
	print "\nWhat do you do?"
	print "1. Scratch dog.\n2. Sit on dog until it goes away. This is now your basket."

	dog_bugging = raw_input("> ")

	if dog_bugging == "1":
		print "He barks at you. You hiss."
		print "The dog runs away. Good job!"
	elif dog_bugging == "2":
		print "Doggy. Doggy friend. Prrrrrrrrr."
		print "Good job!"
	else:
		print "The dog is upset. It eats you because you're a cat."
		print "*** The End ***"


def cat_milk():
	print "You take a sip of the milk in the kitchen. Mjummie!"
	time.sleep(0.5)
	print color.RED + "OH NO! The milk appears to be",
	print color.BOLD + "past the due date!!!!" + color.END
	print "\n"
	time.sleep(0.5)
	print "QUICK! You run to the Persian carpet and puke."
	print "A hairball comes out, along with the milk you just drank."
	time.sleep(0.75)

	dying = "\nHRGRUGRGHGRIURHGRUHHURGHUGRHUGRHURGGRRGUHGRU UUUUUUGEHUHGRH."
	print dying, dying
	print "\nMuch better!\nHEY! There's milk. Let's drink it."

	catmilk_dead()

def cat_life():
	print "So much to do! Where do we start?"
	time.sleep(0.5)
	print "1. Drink milk."
	time.sleep(0.5)
	print "\n2. Sleep."
	time.sleep(0.5)
	cat_choice = raw_input("\nPlease choose 1 or 2: ")

	if cat_choice == "1":
		cat_milk()
	elif cat_choice == "2":
		cat_sleep()
	else:
		print "Miauuuuuuwwww!" # make miauw in banner style from r to l!!


cat_life() # beginning of story line






