from sys import exit

from player import Player
from actions import *


class Engine(object):

	def __init__(self, scene_map):

		self.scene_map = scene_map

	def play(self):

		current_scene = self.scene_map.opening_scene()
		player = Player()

		while player.is_alive():
			current_scene.modify_player(player)
			# Check again since the room could have changed the player's state
			if player.is_alive():

				current_scene = self.scene_map.next_scene(current_scene.enter())

				print "Choose an action: "
				available_actions = current_scene.available_actions()

				for action in available_actions:
					print action
				action_input = raw_input('Action: ')

				for action in available_actions:
					if action_input == action.hotkey:
						player.do_action(action, **action.kwargs)
						break



