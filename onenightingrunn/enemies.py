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


class Heaumeau(Enemy):
	def __init__(self):
		super().__init__(name="Heaumeau", hp=10, damage=2)

class Kabouter(Enemy):
	def __init__(self):
		super().__init__(name="Kabouter", hp=10, damage=2)
# and another class for each enemy like that