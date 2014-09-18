# function to perform the test "FizzBuzz" as described by Jeff Atwood

def fizzbuzz ():

	"""run through numbers 1-100 and then print out fizzbuzz for numbers
	divisible by 3 and 5, fizz for numbers divisible by 3, and buzz by 
	numbers divisible by 5. """

	for nums in range(101):
		if nums%5==0 and nums%3==0 : print "Fizzbuzz" 
		elif nums%5==0 : print "Buzz"
		elif nums%3==0 : print "Fizz"
		else: print nums
	return None


# run the function to test that what is printed out is correct.
fizzbuzz()