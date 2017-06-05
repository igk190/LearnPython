from engine import *

class Map(object):

	scenes = {
	'sleeping_owner': SleepingOwner(),
	'table_blocking_kitchen': TableBlockingKitchen(),
	'hidden_cupboard': HiddenCupboard(),
	'lid_on_snackbox': LidOnSnackbox(),
	'cat_smacking': CatSmacking(),
	'which_cookie_box': WhichCookieBox(),
	'victory': Victory()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

# start scene is passed to the Map class during instantiation

a_map = Map('sleeping_owner')
a_game = Engine(a_map)
a_game.play()