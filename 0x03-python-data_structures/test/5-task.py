def remove_c_from_string(d_str):
    '''
        The function removes uppercase c or lowercase c from a string
    '''
    new_str = ''
    for char in d_str:
        if char == 'c' or char == 'C':
            print('--> c here')

        else:
            new_str += char

    return new_str


def no_c(my_string):
    '''
    Using the translate method to do same operation, this prevents me from
    using a loop.

    Translate():
        To the best of my knowledge the translate function takes a single
        argument which should be a "key value" pair or a table and does
        find and replace on a string.

        Meaning it finds the key UNICODE in the string and replace with
        the value which should be a string.

        I also Noticed that if the value isn't a string it just deletes
        the key from the string which is same as using None object as value.

        maketrans() can also be used to create this "key value" pair
    '''
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    new_str = my_string.translate({ord('c'): None, ord('C'): None})

    return new_string, new_str


print(remove_c_from_string('Best School'))
print(no_c('Best School'))
ret_str = no_c('Best School')
print('returned string: {}\nType: {}'.format(ret_str, type(ret_str)))
