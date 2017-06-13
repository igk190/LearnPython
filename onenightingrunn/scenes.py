from sys import exit
from random import randint

import items, enemies, actions



class Scene(object):

	def enter(self): # intro_text
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

	def modify_player(self, the_player):
		"""Process actions that change the state of the player"""
		raise NotImplementedError()

	def available_actions(self): #unsure if needed
		"""Returns all of the available actions in this room."""
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())

		return moves



class DeUB(Scene):

	def enter(self):
		print "Test scene 1"
		exit(1)

	def modify_player(self, the_player):
		# Room has no action on player
		pass


class Mitra(Scene):

	def enter(self):
		pass


class HotelJoe(Scene):

	def enter(self):
		pass


class BrokenSpeakers(Scene):

	def enter(self):
		pass


class TheQueue(Scene):

	def enter(self):
		pass


class GarderobeFull(Scene):

	def enter(self):
		pass


class AngryBouncer(Scene):

	def enter(self):
		pass


class TheDanceFloor(Scene):

	def enter(self):
		pass


class HappyHourNearlyOver(Scene):

	def enter(self):
		pass


class FriendlyFlatmates(Scene):

	def enter(self):
		pass


class HouseParty(Scene):

	def enter(self):
		pass



class TheSituation(Scene):

	def enter(self):
		pass


class BlauweEngel(Scene):

	def enter(self):
		pass


class HetCorpsHuis(Scene):

	def enter(self):
		pass


class Ziekenhuis(Scene):

	def enter(self):
		pass


class Rumba(Scene):

	def enter(self):
		pass


class DeDrieGezusters(Scene):

	def enter(self):
		pass


class SevenAM(Scene):

	def enter(self):
		pass


class Bienvenue(Scene):

	def enter(self):
		pass
