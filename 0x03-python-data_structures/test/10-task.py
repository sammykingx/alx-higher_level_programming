def divisible_by_2(my_list=[]):
    '''
        A fnction that checks for all multiples of 2 in list where am assuming
        elements of the list are integers.
    '''

# Method 1 using range and len
    '''
    if len(my_lst) == 0:
        return my_lst

    new_list = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
            print('True part -> ', new_list)
        else:
            new_list.append(False)
            print('False part --> ', new_list)

    '''
# Method 2 (using the list itself as the iterable)
    '''
    if len(my_list) == 0:
        return my_list

    for element in my_list:
        if element % 2 == 0:
            new_list.append(True)

        else:
            new_list.append(False)
    '''
# Method 3: Using comprehension
    '''
        comprehension block
    '''
    if len(my_list) == 0:
        return my_list

    new_list = [True if element % 2 == 0 else False for element in my_list]

    return new_list


# Testing with a non empty list

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
print('--------------------------')

# Testing with an empty list

my_list = []
print(my_list)
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
