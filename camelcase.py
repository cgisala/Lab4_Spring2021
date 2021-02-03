# This program turns a sentence into camel case.

import unittest


def camel_case(sentence):
    """ Convert sentence to camelCase, for example, "Display all books" 
    is converted to "displayAllBooks" """
    title_case = sentence.title() # Uppercase firts letter of each word
    upper_camel_cased = title_case.replace(' ', '') # remove spaces
    # Lowercase first letter, join     with rest of string
    #Slices don't produce index out of bounds errors.
    #So this still works on empty strings, strings of length 1
    upper_camel_cased = symbol_filter(upper_camel_cased) # removes symbols
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

#Filters symbols from the sentence
def symbol_filter(sentence):
    unfiltered = []
    filtered = ""
    for n in sentence:
        if n.isalnum():
            unfiltered.append(n)
    for n in unfiltered:
        filtered += n
    return filtered

def main():
    sentence = input('Enter your sentence: ')
    output = camel_case(sentence)
    print(output)

if __name__ == '__main__':
    main()