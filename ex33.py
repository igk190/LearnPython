import time
numbers = []
b = 54

def adding_up(x):
	i = 0
	while i < b:
	    print "\n\nAt the top i is %d" % i
	    numbers.append(x)
	    print "Now numbers consists of: %s" % numbers
	    print "The sum of all numbers in the list is: ", sum(numbers)

	    i += x

	    print "At the bottom i is %d" % i
	    time.sleep(0.3)


adding_up(6)


def adding_up_again(x):
	print "\n\nLET'S DO THAT AGAIN!\n"
	time.sleep(0.8)

	i = 0
	for i in range(0, b):
	    print "\n\nAt the top i is %d" % i
	    numbers.append(x)
	    print "Now numbers consists of: %s" % numbers
	    print "The sum of all numbers in the list is: ", sum(numbers)

	    i += x

	    print "At the bottom i is %d" % i
	    time.sleep(0.3)

adding_up_again(6)