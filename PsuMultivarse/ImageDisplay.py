'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --
This class takes a 2d array of points and visualises it using matplotlib
The image is printed out in the format of an html file
 '''


import math
import numpy as np
from PsuMultivarse import MatrixInvariant as mi

class ImageDisplay:

    def __init__(self,valueslist, commentlist):
        '''
        :param valueslist: a vector of matrices of values to visualise
        :param commentlist: for each values matrix a matching comment
        '''
        self.valueslist = valueslist
        self.commentlist = commentlist

    def visualise(filename, colour, contours):
        #1. using the given colours and contours, visualises in matpploblib
        #2. writes to a file as html
        return 0