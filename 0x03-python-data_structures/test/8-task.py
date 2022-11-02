def multiple_returns(string):
    '''
        The function returns the length of a string and the first character of
        the string in a tuple.

        @String:
            A variable holding the string argument to be operated upon
    '''
    if len(string) == 0:
        temp_tuple = 0, 'None'

    else:
        temp_tuple = len(string), string[0]

    return temp_tuple

# Testing with a non empty string
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}\n----------".format(length, first))

# Testing with an empty string
sentence = ''
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
