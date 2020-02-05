"""Generate Markov text from text files."""
from random import choice

# function to open a text file and return all the text lines merged into just one string:
def open_and_read_file(file_path):
    content = open(file_path).read()
    return content


# using the input_path variable to hold the name of the text file we're feeding into our newly defined function:
file_name_or_path = "green-eggs.txt"

# calling the function we just defined to convert the text of our chosen file and return it as one long string.
# also assigning the string returned to the variable text_string. 
# the value assigned to text_string will be fed into our next function, once we define and call it below.
text_string = open_and_read_file(file_name_or_path)


"""Next we're defining a function that takes input formatted as one long string 
and returns a dictionary of Markov chains formatted as key:value pairs. 
Example of key and value formats to be created:
key ------>   (text_string[0], text_string[1])
value ---->  [text_string[2]]
"""
def make_chains(text_string):
    # create an empty dictionary to use later:
    chains = {}
    # take our long text-string, split it on the space character. 
    # assign the list returned to the variable called words.
    words = text_string.split()
    # create a range to supply our loop with the index numbers of our list items
    # range begins at index 0 but does not include the indexes of our last two list items
    # last two indexes are unnecessary because you need to use three indexes at a time 
    # to produce or update a key:value pair in this code.
    # Also, if we tried to produce or update a key:value pair that started with either of the last two indexes in the list,
    # the code would generate an index number larger than any that actually exist in our list
    # and Python would get upset and stop the program.
    # Now we're going to loop through the index numbers provided by our range:
    # calling the associated strings into our key:value pair format:
    for i in range(len(words)-2):
        key = (words[i], words[i + 1])
        value = (words[i + 2])
        
        # if the current value of key is not yet in our chains dictionary:
        # create a new key with the current value of key
        # create an associated value that's a blank list, which we'll use in the next step
        if key not in chains:
            chains[key] = []

        # call up the current value, which is a list: example_dictionary[example_key]
        # example_dictionary[example_key] will evaluate to example_value, which is a list
        # once we've called up the key's linked value list
        # append our current version of value to that list of values associated with that key
        # this will eventually create our dictionary, chains, one loop at a time
        chains[key].append(value)
    # return the dictionary we've created so we can feed it into the next function:   
    return chains

# calling the make_chains function and assigning the value returned to the variable chainsDictionary
# this variable will be fed into our next function after we've defined and called it in the next step:
chainsDictionary = make_chains(text_string)


""" Next step is to define the function that will take in our dictionary and use it to return a randomly generated string."""
def make_text(chainsDictionary):
    # creating a blank list to load text into later:
    word_list = []
    # randomly selecting a key from our dictionary to start the generation process:
    current_key = choice(list(chainsDictionary.keys()))
    # adding our initial key to the end of our formerly blank word_list:
    word_list.extend(list(current_key))


    # looping to create and add all subsequent values and make the next key in line.
    # loop will terminate once makes a new key that doesn't actually exist in our dictionary:
    while current_key in chainsDictionary.keys():
        # randomly selecting a word-string from the value-list attached to our current_key:
        word_from_value_list = choice(chainsDictionary[current_key])
        # adding the newly chosen value of word_from_value_list to the end of our word_list:
        word_list.append(word_from_value_list)

        # formatting a new key for the next iteration of this loop. 
        # Formatting: ((2nd word of old key), (word_from_value_list that was selected above))
        current_key = (current_key[1], word_from_value_list)
       
    #post-loop wrap-up:
    # use the join method to combine our all the word-strings in our list 
    # into a single string with a space between each word-string:
    # Format of join method to join with a space --->  " ".join(name_of_iterable_to_be_joined)
    outputstring = " ".join(word_list)
    return outputstring


#Call the funtion that was just defined, and print the string it returns:
print(make_text(chainsDictionary))





"""
what follows are miscellaneous note fragments.
They can be ignored unless you're looking for something specific that may have been moved down here.

# Produce random text
#random_text = make_text(chains)

#print(random_text)"

Notes in progress (variable names may not entirely match ours)

#input_path = "green-eggs.txt"

#print(type(open_and_read_file(input_path)))


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
"""
