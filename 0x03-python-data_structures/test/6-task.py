def print_matrix_integer(matrix=[[]]):
    '''
        Print_matrix_integer prints the elemens of a nested list in matrix
        form.

        According to the requirements a space should be printed only between
        elements of a row and the last element of the row should not have a
        space printed after the element is printed
            e.g 1 2 3$

            not 1 2 3 $

            where $ is signifying EOL
    '''
    for x in matrix:
        for y in x:
            print('{:d}'.format(y), end='' if y == x[-1] else ' ')
        print('\n-----')


tst_mtrx = [

        [1, 2, 3],

        [4, 5, 6],

        [7, 8, 9]

        ]
print_matrix_integer(tst_mtrx)
