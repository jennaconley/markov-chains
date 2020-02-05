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

#calling make_chains function and assigning it to t+he variable chains
chains = make_chains(text_string)



def make_text(chainsDictionary):
    """Return text from chains."""

    #Create a blank list to load text into later:
    word_list = []
    #randomly select starting value for key:
    current_key = choice(list(chainsDictionary.keys()))
    #add both of values in key to end of word_list:
    word_list.extend(list(current_key))


    #Loop:
    while current_key in chainsDictionary.keys():
        #randomly select an item from the value list attached to current_key:
        word_from_value_list = choice(chainsDictionary[current_key])
        #add the new value of word_from_value_list to end of wordlist:
        word_list.append(word_from_value_list)

        #format new key for next cucle of loop: ((2nd word of old key), (word_from_value_list that was selected above))
        current_key = (current_key[1], word_from_value_list)
       
    #post-loop wrap-up:
    

    # use method to add list values into a string with a space between each:
    # join method --->  " ".join(name_of_iterable_to_be_joined)

    outputstring = " ".join(word_list)
    return outputstring



#Call the funtion that was just defined:
print(make_text(chains))



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
