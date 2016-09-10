people = 2   # declare var and give it the value of 2
cars = 1  # declare var and give it the value of 1
trucks = 9  # declare var and give it value of 9


if cars > people:   #if statement, runs code block below if true
	print "We should take the cars." # prints a string
elif cars < people:   # else if statement, will run code block below if the if-statement was false
	print "We should not take the cars."  # prints a string
else:   # runs code below if if and else-if statements were false
	print "We can't decide."  # prints a string


if trucks > cars:   # if statement, compares vars trucks with cars, runs code block below if true
	print "That's too many trucks." # prints a string
elif trucks < cars: # else-if statement, compares two vars, runs code block below if true
	print "Maybe we could take the trucks." # prints a string
else: # runs code block below if neither if and else-if statements were true: final alternative
	print "We still cannot decide." # prints a string

if people > trucks: # compares vars people with trucks, if value stored in people is larger than value stored in trucks, code block below is run
	print "Alright, let's just take the trucks." # again, prints a string
else: # runs code if first comparison was false
	print "Fine, let's stay home then." # prints a string


if trucks > people or cars:
	print "\nI am a big truck."
else:
	print "\nMaybe I am not a big truck. The people and cars will not fit in me."