def modify_list(d_lst, idx, elem):
    '''
        The function modifies a mutable sequence at index idx with the value
        elem.

    @d_lst: The mutable sequence
    @idx: The index of the mutable sequence to be modified
    @elem: The value to modify list to at index idx
    '''
    if idx < 0 or idx > len(d_lst) - 1:
        return d_lst

    d_lst[idx] = elem
    return d_lst


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = modify_list(my_list, idx, new_element)

print(new_list)
print(my_list)
