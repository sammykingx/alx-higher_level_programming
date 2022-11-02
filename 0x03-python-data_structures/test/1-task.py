def print_element(my_list, idx):
    '''
        Print_element returns the value of a sequence to the calling function.

    Behaviour:
                When idx is negative or is greater than the length of the
                sequence, the Function returns None else it returns the value
                of the sequence at index idx
    '''
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]


my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, print_element(my_list, idx)))
