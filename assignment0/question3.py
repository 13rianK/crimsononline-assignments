def is_element(x, list) : 
	for y in range(list) :
		if y == x :
			return False
			break
	True

def sortcat (n, *strs) : 

	final_string = ""

	sorted_list = sorted(strs, key=len, reverse=True)

	if n < 0 :
		print ''.join(sorted_list)
		return
	else :
		for i in range(n) : 
			final_string = final_string + sorted_list[i]

	print final_string

	return

sortcat(2, "hello","world","a")