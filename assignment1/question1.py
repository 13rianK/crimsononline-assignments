"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""

#import key libraries
import string


def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """

    #open and read in the filename and then close the file
    f = open(filename)
    words = f.read().split
    f.close()

    # create dictionary for the word count
    wordcount = {}

    # loop over the words counting them
    for word in words :
        wordcount.get(word, 0) + 1

    return sorted(wordcount.keys(), key= lambda count : wordcount[count], reverse=True)

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """

    #use previous functiont to get sorted dict
    lst = common_words(filename)

    for element in lst :
        if element.len() < min_chars : lst.remove(element)

    return lis

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    
    #use previous function to get sorted dictionary with minimums removed
    lst = common_words_min(filename, min_chars)

    return [(word, count) for word, count in lst.iteritems()]



def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try : 
        common_words_tuple(filename, min_chars)
    except IOError :
        print "Error: IOError"

    return