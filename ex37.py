import random

keywords = {

	"and": "Logical and.",
	"as": "Part of the with-as statement.",
	"assert": "Assert (ensure) that something is true.",
	"break": "Stop this loop right now.",
	"class": "Define a class.",
	"continue": "Don't process more of the loop, do it again.",
	"def": "Define a function.",
	"del": "Delete from dictionary.",
	"elif": "Else if condition.",
	"else": "Else condition.",
	"except": "If an exception happens, do this.",
	"exec": "Run a string as Python.",
	"finally": "Exceptions or not, finally do this no matter what.",
	"for": "Loop over a collection of things.",
	"from": "Importing specific parts of a module.",
	"global": "Declare that you want a global variable.",
	"if": "If condition.",
	"import": "Import a module into this one to use.",
	"in": "Part of for-loops. Also a test of X in Y.",
	"is": "Like == to test equality.",
	"lambda": "Create a short anonymous function.",
	"not": "Logical not.",
	"or": "Logical or.",
	"pass": "This block is empty.",
	"print": "Print this string.",
	"raise": "Raise an exception when things go wrong.",
	"return": "Exit the function with a return value.",
	"try": "Try this block, and if exception, go to except.",
	"while": "While loop.",
	"with": "With an expression as a variable do.",
	"yield": "Pause here and return to caller."

}

def do_test():
	testy = True
	randomkeyword = random.choice(keywords.keys())


	values = keywords.get(randomkeyword)
	print "Guess the keyword! The description is: ", values

	while testy:
		guess = raw_input("Guess the word: ")
		if guess == randomkeyword:
			print "Correct guess, the keyword is \"%s\"\n" % randomkeyword
			del keywords[randomkeyword]
			bla = False

			do_test()

		else:
			print "Try again."

do_test()





