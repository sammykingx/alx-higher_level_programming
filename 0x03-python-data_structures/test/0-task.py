'''

    The purpose of this file is to print out all elements of a list
    in a single line according to the ALX learning curriculum

'''


def print_lst_elements(lst=[]):
    '''
        A function that prints out all elements of a sequence in a single line

    lst:
            This parameter holds the arguements passed to the function which
            it's elements is then printed.

    Behaviour:
                When no argument is passed to the function the default value
                which is an empty list is initiated

                When argument is passed and it's type is not an iterable,
                TypeError is raised.

    Author: sammykingx
    '''
    for lst_elem in lst:
        print(lst_elem)


def print_list_integer(my_list=[]):
    '''
        The function prototype given by ALX to print elements of a list
        using str.format().

        A ValueError is raised when the elements of iterable is not of type int

    my_lst:
        Contains the list to prints it's elements which it's type
        must be an iterable.
    '''
    for lst_elem in enumerate(my_list, 0):
        print("{}".format(lst_elem))
    print(type(lst_elem), '>>', enumerate(my_list))


numb = list(range(5))
print(numb)

# calling print_int_elements function
print_lst_elements(numb)
print('***** Done printing my own format, next up is ALX function ******')

# Calling print_list_integer function
print_list_integer(numb)
print('=============\n', hex(id(numb)), enumerate(numb))
