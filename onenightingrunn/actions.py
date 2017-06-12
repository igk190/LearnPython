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
		self.name = name
		self.hotkey = hotkey
		self.kwargs = kwargs  # ?

	def __str__(self):
		return "%s: %s" % (self.hotkey, self.name)


class ViewInventory(Action):
	"""Prints the player's inventory"""
	def __init__(self):
		super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')


class Attack(Action):

	def __init__(self, enemy):
		super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

# Ommitted Flee(Action)