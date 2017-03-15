#This code is meant to simulate a magic 8-Ball, a toy used in fortune telling or seeking advice
#original code only has 8 answers an actual magic 8-ball has 20.Language used - Python


#Here we import the modules
import sys #import searches for the module 'sys' and binds the results of that name into a local scope. Sys provides access to some 
			#used or maintained by the interpreter or that interactly strongly with the interpreter.
import random #random module implements pseudo-random number generator for various distribution		

ans = true #creates a variable named ans and assigns the boolean value True to it.

while ans:
	question = raw_input("Ask the magic 8 ball a question: (press enter to quit)")  #prints a string of characters and assigns user input to questions
	
	answers = random.randint(1,20) #assigns the variable answers a random integer value between 1 and 8
	
	if question =="":
		sys.exit()
	
	elif answers == 1:
		print "It is certain."
	
	elif answers == 2:
		print "It is decidely so"
	
	elif answers == 3:
		print "Without a doubt."
	
	elif answers == 4:
		print "Yes definitely"
		
	elif answers == 5:
		print "You may rely on it"
		
	elif answers == 6:
		print "As I see it, yes"
		
	elif answers == 7:
		print "Most likely"
	
	elif answers == 8:
		print "Outlook good"
		
	elif answers == 9:
		print "Yes"
		
	elif answers == 10:
		print "Signs point to yes."
		
	elif answers == 11:
		print "Reply hazy try again"
		
	elif answers == 12:
		print "Ask again later"
		
	elif answers == 13:
		print "Better not tell you now"

	elif answers == 14:
		print "Cannot predict now"
		
	elif answers == 15:
		print "Concentrate and ask again"
		
	elif answers == 16:
		print "Don't count on it"
		
	elif answers == 17:
		print "My reply is no."
		
	elif answers == 18:
		print "My sources say no."
		
	elif answers == 19:
		print "Outlook not so good."
		
	elif answers == 20:
		print "Very doubtful"
		
#Answers are affirmative, 5 are negative, and 5 are non-commital. Source of idea: https://en.wikipedia.org/wiki/Magic_8-Ball