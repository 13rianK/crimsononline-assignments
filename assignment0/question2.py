import string

def swapchars (sentence):

	c_min = min(string.letters, key=sentence.count)
	c_max = max(string.letters, key=sentence.count)
	c_inter = "~"

	sentence1 = sentence.replace(c_max, c_inter)
	sentence2 = sentence1.replace(c_min, c_max)
	sentence3 = sentence2.replace(c_inter, c_min)

	print sentence3

	return

word = 'hello world! it is a beautiful day outside. I hope to go running today!'

swapchars(word)
