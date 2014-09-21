def max_char (dict, max):
	for char in dict :
		if dict[char] == max : return char

def min_char (dict, min):
	for char in dict :
		if dict[char] == min : return char

def is_alph(char) :
	if 65 <= char and 90 >= char : return True
	elif  97 <= char and 127 >= char : return True
	else : return False

def swapchars (string):
	alph = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,
			'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

	for char in string :
		if is_alph(char) : alph[char] = alph[char] + 1
	
	max = 0
	min = 123456789

	for key in alph :
		if alph[key] > max : max = alph[key]
		if alph[key] > 0 : 
			if alph[key] < min : min = alph[key]

	c_max = max_char(alph, max)
	if min != 123456789 : c_min = min_char(alph, min)
	else: c_min = min_char(alph, 0)

	string1 = string.replace(c_max, c_min)
	string2 = string1.replace(c_min, c_max)

	print string

	return

word = 'hello world'

swapchars(word)
