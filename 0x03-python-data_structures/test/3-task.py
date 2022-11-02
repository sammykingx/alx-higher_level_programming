def print_list_in_rev(d_lst):
    '''
        The function prints out an iterable in reverse without altering
        the elements of the iterable.
    d_lst:
            The iterable whose elements is to be printed in reverse
    '''
    if len(d_lst) == 0:
        return d_lst

    for element in range(len(d_lst)):
        print('{:d}'.format(d_lst[len(d_lst) - 1 - element]), end='')

    print()


my_list = list(range(1, 6))
print('BEFORE FUNC_CALL: ', my_list)
print_list_in_rev(my_list)
print(my_list)
