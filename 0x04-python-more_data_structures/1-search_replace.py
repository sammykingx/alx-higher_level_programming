#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
        A function that traverse through a list for an element that matches
        search and modify it with replace then returns a new list.

    '''
    if len(my_list) == 0:
        return my_list

    new_lst = [element if element != search else replace for element in my_list]
    return new_lst


# Test
my_lst = [1, 2, 3, 4, 5, 7, 8]
print(my_lst)
print(search_replace(my_lst, 2, 89))

