from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = int(raw_input("> "))

	# simplified
	if 0 <= choice <= 50:
		print "Nice, you're not greedy, you win!"
		next_room()
	elif choice > 50:
		dead("You greedy bastard!")
	else:
		dead("Man, learn to type a number.")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		# easier to overlook
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
			print "What now?"
			bear_moved = False

			bearchoice = raw_input("> ")

			if bearchoice == "taunt bear":
				dead("The bear gets pissed off and chews your leg off.")
			elif bearchoice == "open door":
				bear_moved = True
				gold_room()
			else:
				print "I got no idea what that means."

		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you se the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def next_room():
	print "You see a fountain and a sign saying 'please do not jump in the fountain.'"
	print "There's also a chair. What do you do?"

	danger_zone = raw_input("> ")

	if "swim" in danger_zone or "jump in" in danger_zone:
		dead("Oh no! The water is contaminated. You die =(.")
	elif "sit" in danger_zone and "chair" in danger_zone:
		print "You grab a nearby newspaper. You read it."
		print "WAITAH! WHERE MY CIGARS AT!"
		exit(0)


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()