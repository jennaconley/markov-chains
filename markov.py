"""Generate Markov text from text files."""
from random import choice

def open_and_read_file(file_path):
    content = open(file_path).read()
    return content


input_path = "green-eggs.txt"

text_string = open_and_read_file(input_path)



def make_chains(text_string):
    chains = {}
    words = text_string.split()
    for i in range(len(words)-2):
        key = (words[i], words[i + 1])
        value = (words[i + 2])
        
        if key not in chains:
            chains[key] = []

        chains[key].append(value)
        #print(key, chains[key])
    #print(chains)
     
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:
        >>> chains = make_chains("hi there mary hi there juanita")
    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())py
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """
    
    # your code goes here
    return chains

#calling make_chains function and assigning it to the variable chains
chains = make_chains(text_string)



def make_text(chainsDictionary):
    """Return text from chains."""

    wordList = []

#randomly select first key pop()??

#add first key to wordList

#A. chose a word (randomly within that key's value list) to follow key

#append new word to output list: wordList

#look for a new key: (2nd word of old key, new word)
#if (2nd word of old key, new word) in chainsDictionary go back to A and repeat steps







    # anystring.join(name_of_iterable_to_be_joined)
    return "our_markov_string".join(wordslist)



# Produce random text
#random_text = make_text(chains)

#print(random_text)"





"""
Notes in progress (variable names may not entirely match ours)

#input_path = "green-eggs.txt"

#print(type(open_and_read_file(input_path)))


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
"""
