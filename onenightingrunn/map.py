#from random import randint # do we need this? in THIS file?neee
from scenes import *
from game import * 

class Map(object):

	scenes = {
	'de_ub': DeUB(),
	'mitra': Mitra(),
	'hotel_joe': HotelJoe(), # pick drinks, they'll do either health || damage
	'broken_speakers': BrokenSpeakers(),
	'the_queue': TheQueue(),
	'garderobe_full': GarderobeFull(),
	'angry_bouncer': AngryBouncer(),
	'the_dancefloor': TheDanceFloor(),
	'happy_hour_nearly_over': HappyHourNearlyOver(),
	'friendly_flatmates': FriendlyFlatmates(), # speakers | houseparty
	'houseparty': HouseParty(), # damage
	'the_situation': TheSituation(),
	'blauwe_engel': BlauweEngel(), # the 'death' scene
	'het_corps_huis': HetCorpsHuis(),
	'ziekenhuis': Ziekenhuis(),
	'rumba': Rumba(),
	'de_drie_gezusters': DeDrieGezusters(),
	'seven_am': SevenAM(),
	'bienvenue': Bienvenue()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('de_ub')
a_game = Engine(a_map)
a_game.play()
