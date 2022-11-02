def max_integer(my_list=[]):
    '''
        Function that returns the largest integer in a list
    '''
# Method 1
    my_list.sort()
    print(my_list)
    return my_list[-1]
'''
# Method 2

    if len(my_list) == 0:
        return "None"

    max_int = my_list[0]
    for elements in my_list:
        if elements > max_int:
            max_int = elements
    return max_int
'''

'''
# Method 3
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
'''


my_list = [1, 90, 2, 13, 34, 5, -13, 133]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
