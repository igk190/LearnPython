import random
import items


class Player(object):

	def __init__(self):
		self.inventory = [items.Gold(15), items.Rock()]
		self.hp = 100

	def is_alive(self):
		return self.hp > 0

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)

	def print_inventory(self):
		for item in self.inventory:
			print item, '\n'

	def attack(self, enemy):
		best_weapon = None
		max_dmg = 0
		for i in self.inventory:
			if isinstance(i, items.Weapon):
				if i.damage > max_dmg:
					max_dmg = i.damage
					best_weapon = i

		print "You use %s against %s!" % (best_weapon.name, enemy.name)
		enemy.hp -= best_weapon.damage
		if not enemy.is_alive():
			print "You killed %s!" % (enemy.name)
		else:
			print "%s HP is %s." % (enemy.name, enemy.hp)

