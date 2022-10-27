def new_list(d_lst, idx, element):
    '''
        A function that replaces an element of a list at a particular index
        without modifying the original list.

        @d_lst:
            The variable containing the listpassed as arguements

        @idx:
            The index of the element to replace in d_lst

        @element:
            The value to place at index 'idx'
    '''
    if idx < 0 or idx > len(d_lst) - 1 or len(d_lst) == 0:
        print('empty')
        return d_lst.copy()

    new = d_lst.copy()
    new[idx] = element
    return new


nw = list(range(1, 6))
# nw = []
print('Original list: ', nw)
print(f'New list: {new_list(nw, 3, 9)}')
