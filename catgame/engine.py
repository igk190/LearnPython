from sys import exit
from random import randint

class Engine(object):

	def __init__(self, scene_map):
		#print "Engine __init__ has scene_map", scene_map
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		# last_scene = self.scene_map.next_scene('cat_smacking')
		print "Play first scene:", current_scene

		while True:
	#		next_scene_name = current_scene.enter() # here's where you start playing
	#		current_scene = self.scene_map.next_scene(next_scene_name) # without this eternal loop
			#print "map returns new scene", current_scene
			current_scene = self.scene_map.next_scene(current_scene.enter())
		#return current_scene.enter()





class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

class CatSmacking(Scene):

	def enter(self):
		print """
		\nOopsie. The dog just came back home. You get scared
		and hide. No treats for you today.
		"""
		exit(1)

class SleepingOwner(Scene):

	def enter(self):
		print """\nYou must get off lap without waking the owner.
		What do you do?"""

		action = raw_input("> ")

		if "scratch" in action:
			print "\nUh oh! You shouldn't have."
			return 'cat_smacking'
		elif "tip toe" in action:
			print "\nYou did it! You moved without waking the owner."
			return 'table_blocking_kitchen'
		else:
			print "Huuuuuuh."
			return 'sleeping_owner'

class TableBlockingKitchen(Scene):

	def enter(self):
		print "\nAy. Big obstacle blocking the path. What now?"

		dilemma = raw_input("> ")

		if "jump" in dilemma:
			print "\nGreat! You're a cat so you used jump."
			print "You jumped over the obstacle. Score."
			return 'hidden_cupboard'
		else:
			"vYou hit your head lol. You lose an eye."
			return 'cat_smacking'

class HiddenCupboard(Scene):

	def enter(self):
		print "\nThe kitchen has been invaded. You sharpen your vision."
		print "The mission: find the hidden cabinet!!!"

		find_cabinet = raw_input("> ")

		if "smell" in find_cabinet:
			print "\nYou're an animal. You follow your senses and"
			print "find the cabinet. Getting closer!"
			return 'lid_on_snackbox'
		elif "walk" in find_cabinet:
			print "\nYou walk in circles, but find nothing."
			return 'hidden_cupboard'
		else:
			print "\n???"
			return 'cat_smacking'

class LidOnSnackbox(Scene):

	def enter(self):
		print "\nOh no, a lid! You have no thumbs. How to fix :("

		open_box = raw_input("must retrieve snack> ")

		if "scratch" in open_box and "open" in open_box:
			print "\nYou scratch and scratch until a hole becomes visible."
			print "MUST HAZ COOKIE."
			return 'which_cookie_box'
		elif "hit" in open_box:
			print "\nYou try to hit the box. It is useless."
			return 'cat_smacking'
		else:
			print "\nNo comprendo. No hablo espanol."
			return 'lid_on_snackbox'

class WhichCookieBox(Scene):

	def enter(self):
		print "You silly, all that effort used, but on the wrong cookie box."
		print "Try again, this time, pick the right one. The force may are with you."

		correct_jar_with_cookies = "%d" % (randint(0, 5))
		choice = raw_input("Which boxjarr? There's 5, but only one with f00d. Three tries, go!> ")
		guesses = 0

		while choice != correct_jar_with_cookies and guesses < 2:
			print "Oh no! Wrong. Again?"
			guesses += 1
			choice = raw_input("COOKIEEEE>>> ")

		if choice == correct_jar_with_cookies:
			return 'victory'
		else:
			return 'cat_smacking'

class Victory(Scene):

	def enter(self):
		print "\nNailed it! I HAZ THE COOKIES! VICTORY ARE BELONG TO ME!"
		print "Prrrrrrrr. Mjum. Prrrrrrr. Krr Krr."
		exit(1)
