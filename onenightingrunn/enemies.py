class Enemy(object):
	"""A base class for all enemies"""
	def __init__(self, name, hp, damage):
		"""Creates a new enemy

		:param name: the name of the enemy
		:param hp: the enemy's hit points
		:param damage: the damage the enemy does with each attack
		"""

		self.name = name
		self.hp = hp
		self.damage = damage

	def is_alive(self):
		return self.hp > 0


class Henk(Enemy):
	def __init__(self):
		super().__init__(name="Henk", hp=10, damage=2)

# and one more class for each enemy like that