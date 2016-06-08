import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Baden-Wuerttemberg', 'BW') #1
hashmap.set(states, 'Freistaat Bayern', 'BY') #2
hashmap.set(states, 'Berlin', 'BE') #3
hashmap.set(states, 'Brandenburg', 'BB') #4
hashmap.set(states, 'Bremen', 'HB') #5
hashmap.set(states, 'Hamburg', 'HH') #6
hashmap.set(states, 'Hessen', 'HE') #7
hashmap.set(states, 'Niedersachsen', 'NI') #8
hashmap.set(states, 'Mecklenburg-Vorpommern', 'MV') #9
hashmap.set(states, 'Nordrhein-Westfalen', 'NW') #10
hashmap.set(states, 'Rheinland-Pfalz', 'RP') #11
hashmap.set(states, 'Saarland', 'SL') #12
hashmap.set(states, 'Freistaat Sachsen', 'SN') #13
hashmap.set(states, 'Sachsen-Anhalt', 'ST') #14
hashmap.set(states, 'Schleswig-Holstein', 'SH') #15
hashmap.set(states, 'Freistaat Thueringen', 'TH') #16

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'BW', 'Stuttgart')
hashmap.set(cities, 'BY', 'Muenchen')
hashmap.set(cities, 'BE', 'None')
hashmap.set(cities, 'BB', 'Potsdam')
hashmap.set(cities, 'HB', 'None')
hashmap.set(cities, 'HH', 'None')
hashmap.set(cities, 'HE', 'Wiesbaden')
hashmap.set(cities, 'NI', 'Hannover')
hashmap.set(cities, 'MV', 'Schwerin')
hashmap.set(cities, 'NW', 'Duesseldorf')

# add some more cities
hashmap.set(cities, 'RP', 'Mainz')
hashmap.set(cities, 'SL', 'Saarbruecken')
hashmap.set(cities, 'SN', 'Dresden')
hashmap.set(cities, 'ST', 'Magdeburg')
hashmap.set(cities, 'SH', 'Kiel')
hashmap.set(cities, 'TH', 'Erfurt') ## VANF HIER VERDER

# print out some cities
print '-' * 10
print "HH State has: %s" % hashmap.get(cities, 'HH')
print "HE State has: %s" % hashmap.get(cities, 'HE')
print "NI State has: %s" % hashmap.get(cities, 'NI')
print "MV State has: %s" % hashmap.get(cities, 'MV')
print "NW State has: %s" % hashmap.get(cities, 'NW')


# print some states
print '-' * 10
print "Rheinland-Pfalz's abbreviation is: %s" % hashmap.get(states, 'Rheinland-Pfalz')
print "Saarland's abbreviation is: %s" % hashmap.get(states, 'Saarland')
print "Freistaat Sachsen's abbreviation is: %s" % hashmap.get(states, 'Freistaat Sachsen')
print "Sachsen-Anhalt's abbreviation is: %s" % hashmap.get(states, 'Sachsen-Anhalt')
print "Schleswig-Holstein's abbreviation is: %s" % hashmap.get(states, 'Schleswig-Holstein')


# do it by using the state then cities dict
print '-' * 10
print "Baden-Wuerttemberg has: %s" % hashmap.get(cities, hashmap.get(states, 'Baden-Wuerttemberg'))
print "Freistaat Thueringen has: %s" % hashmap.get(cities, hashmap.get(states, 'Freistaat Thueringen'))


# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Groningen')

if not state:
	print "Sorry, no Groningen."

# default values using //= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'GR', 'Does Not Exist')
print "The city for the state 'GR' is: %s" % city