'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --
This class takes an entire matrix of data, and performs interpolation at any point to a given degree
At the chosen point, a local function is calculated based on the degree using  the MultiSolver or PolySolver
If the points are too close to the edge, the degree will be automatically reduced to enable the interpolation
This allows the calculation of derivtives and values of the data
 '''


import math
import numpy as np
from PsuMultivarse import MatrixInvariant as mi

class Interpolator:

    def __init__(self,values):
        self.values = values
        minv = mi.MatrixInvariant()

    def getValue(self,point, degree):
        #1. First build the appropriate values matric around the point at the given degree
        #2. Then ask for the point from a MultiSolver or PolySolver adjusting it's value to be the centre of the local curve
        return 0