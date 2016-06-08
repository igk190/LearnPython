#Find examples of things in the real world that would fit in a list.
#Try writing some scripts to work with them.
import random


##### 1.
print "\n\n#1. A study to-do list.\n"

to_do = []
total_stuffs = 0

stuff = "Python", "HTML", "CSS", "Sf", "Website for friend"
print "We're gonna add stuff to the list."

to_do.append(stuff)
print "On the daily to-do list we now have: ", stuff

for i in stuff:
	total_stuffs += 1
	print "\nNr. %i on the list is:" % total_stuffs, i




##### 2.
print "\n\n#2. Grocery list\n"
print "It is supermarket time!"
groceries = ['apple', 'banana', 'kiwi', 'milk', 'pear']
print groceries

res = str.format("Please go these at the supermarket: {v[0]}, {v[2]}, {v[3]} and {v[4]}", v = groceries)
print res

Rem = [0,2,3,4]

for i in Rem:
	groceries[i]='!'

for i in range(0,groceries.count('!')):
	groceries.remove('!')
print "These foods are left, go get these next:", groceries




###### 3.
print "\n\n#3. Sports customers."
Henk = {'name': 'Henk','age': 20, 'package': 'PT', 'quantity': 12}
Piet = {'name': 'Piet', 'age': 25, 'package': 'Fitness', 'quantity': 12}
Kees = {'name': 'Kees', 'age': 30, 'package': 'PT', 'quantity': 36}
Frits = {'name': 'Frits', 'age': 21, 'package': 'Fitness', 'quantity': 12}
Jan = {'name': 'Jan', 'age': 22, 'package': 'PT', 'quantity': 12}
Wilma = {'name': 'Wilma', 'age': 29, 'package': 'Fitness', 'quantity': 12}

customers = []

customers.extend((Henk, Piet, Kees, Frits, Jan, Wilma))


print "\n", customers
print "Henk's package is:", Henk['package']
print "Wilma chose this quantity:", Wilma['quantity']
print "Henk's info:", Henk

# how to fetch only all info for vars with "quantity": 12 and display with name?


##### 4.
print "\n\n4. Games!\n"
game = {
    'A': 'Lego Racers',
    'B': 'Bugs Bunny',
    'C': 'Doom',
    'D': 'Rollercoaster Tycoon'
}

gamelist = []
gamelist += game.values()
print "\n\n", gamelist, "\n"

print game['C']
print game['D']
print game.items()[0]
print game.keys()[3]
print game.values()[3]


#####5. Friends.
print "\n\n5. Matties.\n"
named_friends = raw_input("Who are your friends? Name 5. Use first names and separate friends with a space:")
named_friends = named_friends.lower().strip()

friends_separated = named_friends.split(' ')
print "So these are your homeboys and gurls: %s" % friends_separated
print "Today you are going to chill with: %s" % random.choice(friends_separated)
print "Tomorrow you are going to chill with: %s\n" % random.choice(friends_separated)

dayschill = 0
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

while dayschill < 10:
	for day in weekdays:
		print day + ": You're gonna chill with %s" % random.choice(friends_separated)
		dayschill += 1







