# create a mapping of state to abbreviation
states = {
	'Baden-Wuerttemberg': 'BW', #1
	'Freistaat Bayern': 'BY', #2
	'Berlin': 'BE', #3
	'Brandenburg': 'BB', #4
	'Bremen': 'HB', #5
	'Hamburg': 'HH', #6
	'Hessen': 'HE', #7
	'Niedersachsen': 'NI', #8
	'Mecklenburg-Vorpommern': 'MV', #9
	'Nordrhein-Westfalen': 'NW', #10
	'Rheinland-Pfalz': 'RP', #11
	'Saarland': 'SL', #12
	'Freistaat Sachsen': 'SN', #13
	'Sachsen-Anhalt': 'ST', #14
	'Schlewsig-Holstein': 'SH', #15
	'Freistaat Thueringen': 'TH' #16
}

# create a basic set of states and some cities in them
cities = {
	'BW': 'Stuttgart',
	'BY': 'Muenchen',
	'BE': 'None',
	'BB': 'Potsdam',
	'HB': 'None',
	'HH': 'None',
	'HE': 'Wiesbaden',
	'NI': 'Hannover',
	'MV': 'Schwerin',
	'NW': 'Duesseldorf'
}

# add some more cities
cities['RP'] = 'Mainz'
cities['SL'] = 'Saarbruecken'
cities['SN'] = 'Dresden'
cities['ST'] = 'Magdeburg'
cities['SH'] = 'Kiel'
cities['TH'] = 'Erfurt'

# print out some cities
print '-' * 10
print "BW state has: ", cities['BW']
print "BY State has: ", cities['BY']
print "BE State has: ", cities['BE']
print "BB State has: ", cities['BB']
print "HB State has: ", cities['HB']
print "HH State has: ", cities['HH']


# print some states
print '-' * 10
print "Hessen's abbreviation is: ", states['Hessen']
print "Niedersachsen's abbreviation is: ", states['Niedersachsen']

# do it by using the state then cities dict  # ASDLDLSHS
print '-' * 10
print "Mecklenburg-Vorpommern has: ", cities[states['Mecklenburg-Vorpommern']]
print "Nordrhein-Westfalen has: ", cities[states['Nordrhein-Westfalen']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Groningen')

if not state:
	print "Sorry, no Groningen."

# get a city with a default value
city = cities.get('GR', 'Does Not Exist')
print "The city for the state 'GR' is: %s" % city







