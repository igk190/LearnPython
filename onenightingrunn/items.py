"""Describes the items in the game."""


class Item(object):
	"""The base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self): # str?
		return "%s\n=====\n%s\nValue: %s\n" % (
			self.name,
			self.description,
			self.value
			)


class Weapon(Item):

	def __init__(self, name, description, value, damage):
		self.damage = damage
		super(Weapon, self).__init__(name, description, value)
		# check Zed's explanation

	def __str__(self):
		return "%s\n=====\n%s\nValue: %s\nDamage: %s" % (
			self.name,
			self.description,
			self.value,
			self.damage
			)

class Rock(Weapon):

	def __init__(self):
		super(Rock, self).__init__(name="Rock",
						description="A first-sized rock, suitable for bludgeoning.",
						value=0,
						damage=5)


class Dagger(Weapon):

	def __init__(self):
		super(Dagger, self).__init__(name="Dagger",
						description="A small dagger with some rust. Somewhwat more dangerous than a rock.",
						value=10,
						damage=10)


class Gold(Item):

	def __init__(self, amt):
		self.amt = 6
		super(Gold, self).__init__(name="Gold",
						description="A round coin with {} stamped on the front.".format(str(self.amt)),
						value=self.amt)







