class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

verjaardagslied = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

stiertjesparade = Song(["\nThey rally around tha family",
						"With pockets full of shells"])

##
britney_liedje = ["\nOops I did it again",
				"I played with your heart",
				"Got lost in tha game"]

willekeurig_lied = ["\nIk zing een liedje",
					"Pietje Pietje Pietje",
					"La lalalalala"]

verjaardagslied.sing_me_a_song()

stiertjesparade.sing_me_a_song()

its_britney_bitch = Song(britney_liedje)
its_britney_bitch.sing_me_a_song()

liedje_zingen = Song(willekeurig_lied)
liedje_zingen.sing_me_a_song()