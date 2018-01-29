import sys
import random


with open('/usr/share/dict/words') as f:
    content = f.read().split('\n')
    print(content)


def create_histogram(corpus):
    '''
    Creates histogram out of corpus using a dictionary

    Iterates through corpus and checks if word already exists in histogram.

        -- If word does not exist, add word as key with value set to 1.

        -- If word does exist, increment key value by 1.
    '''
    hist = {}
    #begin iterating through corpus
    for word in corpus:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1
    return hist

def dicto_rando(histogram, num_words = 6):
    '''
    Expects a dictionary for histogram argument.
    Expects an int for num_words argument.

    Returns a list of random words from the histogram.
    Generates a random number between 1 and the number of tokens from the
    histogram (uses count_tokens function).

    Loops through key values, summing up the values. As soon as the running total
    is greater than or equal to a random number, add that key to the list that will
    be returned.

    When len(list) == num_words, return list.
    '''
    pass


def show_all_types(histogram):
    '''
    Expects a dictionary object for histogram argument.

    Iterate through dictionary, adding keys to a list. Return list after Loop
    finishes.
    '''
    pass

def count_tokens(histogram):
    '''
    Expects a dictionary object for histogram argument.

    Iterate through dictionary, adding each value to a running total. When loop finishes
    return total.
    '''
    running_total = 0
    for word, val in histogram.items():
        running_total += val

    return running_total


# if __name__ == '__main__':
