"""Describes the actions a player can make in the game"""

from player import Player


class Action(object):
	"""The base class for all actions"""
	def __init__(self, method, name, hotkey, **kwargs):
		"""Creates a new action

		:param method: the function object to execute
		:param name: the name of the action
		:param ends_turn: True if the player is expected to move after this action, else False
		:param hotkey: the keyboard key the player should use to initiate this action
		"""
		self.method = method
		self.hotkey = hotkey
		self.name = name
		self.kwargs = kwargs  # whutt

	def __str__(self):
		return "{}: {}".format(self.hotkey, self.name) # whutt


class ViewInventory(Action):
	"""Prints the player's inventory"""
	def __init__(self):
		super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')


class Attack(Action):

	def __init__(self, enemy):
		super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)


# We might be able to ommit the below.
class Flee(Action):

	def __init__(self, title):
		super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)
	# FIX TILE at end of above

