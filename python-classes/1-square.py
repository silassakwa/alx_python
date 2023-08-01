#!/usr/bin/python3
"""class Square that defines a square"""
class Square:
    """
    represent a class called Square
    """
    def __init__(self,size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """ 
    

        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be greater than zero")
        self.__size=size