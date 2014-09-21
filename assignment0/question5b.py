# test for question1.py
from question1 import fizzbuzz

print "fizzbuzz: "
print(fizzbuzz())

"""For this we expect to see numbers divisible by 3 to say fizz,
numbers divisble by 5 to say buzz, and numbers divisible by both
to say fizzbuzz"""

print

#test for question2.py
from question2 import swapchars

print "swapchars: "
print(swapchars("This is a long sentence with many spaces and characters"))
print(swapchars("This.sentence.has.a.lot.of.punctuation"))
print(swapchars("aaaaaa"))
print(swapchars("this uses the intermediate character, ~~ when replacing"))
"""for the last one we expect the ~~ to be replaced when it shouldn't be because
that is the intermediate character used for swapping. I could not think of a way
around that. For the 2nd test the punctuation is most common character. I could
have created a string devoid off all punctuation and spaces, but that seemed
tedious and unnecessary for the assignment. All the other tests behave as expected"""

print

#tests for question3.py
from question3 import sortcat

print "sortcat: "
print(sortcat(1, "a", "ahhhhh"))
print(sortcat(-1, "a", "ahhhhh"))
print(sortcat(1, "hello", "world", "ign"))
print(sortcat(2, "hello", "world", "ign"))
print(sortcat(3, "hello", "world", "ign"))
print(sortcat(-1, "hello", "world", "ignore"))
print(sortcat(-5, "hello", "world", "ign"))

""" All the outputs are as they are expected. First one should be 'ahhhhh',
second one should be 'ahhhhha, and so on. I did not include a case where
an input was not a string because this creates a TypeError which crashes the
test file. To solve this we could test that all arguments entered are strings
and if they are not return an error. """

print

# show output for question4.py
from question4a import luigi_is_a_boss

print "Luigi: "
print luigi_is_a_boss(1)
print luigi_is_a_boss(10)
print luigi_is_a_boss(100)
print luigi_is_a_boss(1000)
print luigi_is_a_boss(1000)
print luigi_is_a_boss(1000)
print luigi_is_a_boss(1000)
print luigi_is_a_boss(1000)
print luigi_is_a_boss(10000)

""" The general probability for luigi winning is 0.30 """