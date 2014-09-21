#import random module to access random number generator
import random


# function to test if Luigi won the game or not
def luigi_won () :

	# create characters to face off against luigi
	mario = False
	wario = False
	peach = False

	# go through 5 rounds. if they match luigi (who is at constant value 1) 
	# then they lose (go to True)
	for i in range(5) : 
		if random.randint(1,5) == 1 : peach = True
		if random.randint(1,5) == 1 : mario = True
		if random.randint(1,5) == 1 : wario = True

	# if all players are True then Luigi won, else he lost
	if mario == True and peach == True and wario == True : return True
	else : return False	


# function to return percentage of times 
def luigi_is_a_boss (trials) : 

	wins = 0

	# run through n trials, increasing wins by 1 if luigi won the game
	for n in range(trials) : 
		if luigi_won() : wins = wins + 1

	#print a fraction of his wins and return a percentage of his wins
	print "%d/%d" %(wins,trials)

	return wins/float(trials)

print luigi_is_a_boss(100)