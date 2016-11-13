provincies = {
	'Groningen': 'GR',
	'Friesland': 'FR',
	'Drenthe': 'DR',
	'Overijssel': 'OR',
	'Gelderland': 'GL',
	'Flevoland': 'FL',
	'Utrecht': 'UR'
}

# provincies en hoofstad
hoofdsteden = {
	'GR': 'Groningen',
	'FR': 'Leeuwarden',
	'DR': 'Assen',
	'OR': 'Zwolle',
	'GL': 'Arnhem'
}

#voeg meer steden toe
hoofdsteden['FL'] = 'Lelystad'
hoofdsteden['UR'] = 'Utrecht'

# print out some cities
print "\n\nGR heeft: ", hoofdsteden['GR']
print "FR heeft: ", hoofdsteden['FR']
print "DR heeft: ", hoofdsteden['DR']

# print out some provinces
print "\nOverijssels afkorting is: ", provincies['Overijssel']
print "Gelderlands afkorting is: ", provincies['Gelderland']

# eerst provincie dan stad
print "\nGroningen heeft: ", hoofdsteden[provincies['Groningen']]
print "Friesland heeft: ", hoofdsteden[provincies['Friesland']]
print "Drenthe heeft: ", hoofdsteden[provincies['Drenthe']]

#print alle afkortingen
print '-' * 10
for prov, afkorting in provincies.items():
	print "%s is onofficieel afgekort als %s" % (prov, afkorting)

#print de hoofdstad in elke provincie
print '-' * 10
for afkorting, stad in hoofdsteden.items():
	print "%s heeft als stad %s" % (afkorting, stad)

# nu allebei tegelijk
print '-' * 10
for provincie, afkorting in provincies.items():
	print "Provincie %s is afgekort als %s en heeft als stad %s" % (
		provincie, afkorting, hoofdsteden[afkorting])

print '-' * 10
# fetch een afkorting van een provincie dat niet bestaat
provincie = provincies.get('Puffeldorp')

if not provincie:
	print "Sorry, geen Puffeldorp."

# fetch een stad met een default waarde
stad = hoofdsteden.get('Puff', 'Puffeldorp bestaat niet.')
print "De stad voor de provincie Puffeldorp is: %s" % stad


print 'henk' in provincies
print 'GR' in hoofdsteden
print 'Groningen' in hoofdsteden