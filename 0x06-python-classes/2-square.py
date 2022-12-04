#!/usr/bin/python3
''' A Module that creates a Square object '''

class Square;
''' Creating an Object template '''

    def __init__(self, size = 0):
        '''
            The init method initializes the class instance

        @self:
            A parameter used to refer to the class instance

        @size:
            The size of the square, must be a +ve integer
        '''
        if type(size) is int:
            if size < 0:
                raise ValueError('Size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('Size must be an integer')
