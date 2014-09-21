#import the string module for later use
import string

def swapchars (sentence):

	# find the characters that appear minimum and maximum
	c_min = min(sentence.replace(" ", ""), key=sentence.count)
	c_max = max(sentence.replace(" ", ""), key=sentence.count)
	c_inter = "~"

	#go through and swap characters using an intermediary character.
	sentence1 = sentence.replace(c_max, c_inter)
	sentence2 = sentence1.replace(c_min, c_max)
	sentence3 = sentence2.replace(c_inter, c_min)

	print sentence3

	return

"""Important note, I could use string.letters for finding the minimum and 
maximum character occurances in the alphabet, but then it would include letters
not contained in the sentence. I created one that used sentence as its
filter for what to sort, but that included punctuation as well. I decided it
was better to swap with punctuation and spaces then to insert new characters
into the string"""

#test functions can be found in question5b.py
# run the function to test that what is printed out is correct.