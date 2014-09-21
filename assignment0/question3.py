def sortcat (n, *strs) : 

	# create a final output string to append to
	final_string = ""

	# sort through the given string arguments to put in greatest-least order
	sorted_list = sorted(strs, key=len, reverse=True)

	# in case n < 0 join all strings together
	if n < 0 :
		print ''.join(sorted_list)
		return
	# in case n>0 join n longest strings together
	else :
		for i in range(n) : 
			final_string = final_string + sorted_list[i]

	print final_string

	return
