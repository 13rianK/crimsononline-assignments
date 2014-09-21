import random

def luigi_won () :

	mario = False
	wario = False
	peach = False

	for i in range(5) : 
		if random.randint(1,5) == 1 : peach = True
		if random.randint(1,5) == 1 : mario = True
		if random.randint(1,5) == 1 : wario = True

	if mario == True and peach == True and wario == True : return True
	else : return False	



def luigi_is_a_boss (trials) : 

	wins = 0

	for n in range(trials) : 
		if luigi_won() : wins = wins + 1

	print "%d/%d" %(wins,trials)

	return wins/float(trials)

print luigi_is_a_boss(100)