def add_tuple(tuple_a=(), tuple_b=()):
    '''
        The function adds only the first two elements of both tuples and returns
        a tuple containing two elements which are the result from addittion.

        e.g tuple_a = (1, 2, 3)
            tuple_b = (4, 5, 6)

            new_tuple returned would now be (5, 7)
    '''
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

    return new_tuple


tuple_a = (15, 2)
tuple_b = (1, 2)

new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
print('tuple_a After: ',tuple_a)
