from sys import exit
from random import randint

from player import Player


class Engine(object):

	def __init__(self, scene_map):

		self.scene_map = scene_map

	def play(self):

		current_scene = self.scene_map.opening_scene()
		print "Play first scene:", current_scene

		player = Player()
		while Player.is_alive():
			current_scene.modify_player(player)
			# Check again since the room could have changed the player's state
			if player.is_alive():
				current_scene = self.scene_map.next_scene(current_scene.enter())

		# original below
		#while True:
		#	current_scene = self.scene_map.next_scene(current_scene.enter())

