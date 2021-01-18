'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --
This class takes an entire matrix of data, and performs interpolation at any point to a given degree
At the chosen point, a local function is calculated based on the degree using  the MultiSolver or PolySolver
If the points are too close to the edge, the degree will be automatically reduced to enable the interpolation
This allows the calculation of derivtives and values of the data
 '''


import math
import numpy as np
from PsuMultivarse import MultiSolver as ms

class Interpolator:

    def __init__(self,values):
        self.values = values
        self.dims = values.shape
        self.dim = len(values.shape)
        self.sectionset = False
        self.sections = {}

    def pointsSection(self, section):
        '''
        :param section: the sub section of values over which you wish to interpolate
        '''
        self.section = section
        self.sectionset = True

    def getValues(self, point, degree, gap):
        '''
        :param point: the [x] or [x,y] or [x,y,z] tuple
        :param degree: the polynomial fit degree, must be an odd number, 1 is linear, 3 is spline etc
        :param gap: the sample fraction between grid points, between 0 and 1
        :return: a matrix of interpolated values
        '''
        if self.sectionset:
            subvalues = self._getSubValues(point, degree)
            solver = ms.MultiSolver(subvalues)
            return solver.getValue(point)
        return 0

    def getValue(self,point, degree):
        '''
        :param point: the [x] or [x,y] or [x,y,z] tuple
        :param degree: the polynomial fit degree, must be an odd number, 1 is linear, 3 is spline etc
        :return: the interpolated value
        '''
        #1. First build the appropriate values matric around the point at the given degree
        #2. Then ask for the point from a MultiSolver or PolySolver adjusting it's value to be the centre of the local curve
        if not self.sectionset:
            if self.dim == 3:
                subvalues, adjpoint = self._getSubValues3d(point,degree)
            elif self.dim == 2:
                subvalues, adjpoint = self._getSubValues2d(point,degree)
            else:
                subvalues, adjpoint = self._getSubValues1d(point,degree)
            solver = ms.MultiSolver(subvalues)
            return solver.getValue(adjpoint)

        return 0

    #####################################################################
    ###### Internal Functions #########################################
    #####################################################################

    def _getSubValues1d(self,point, degree):
        xcorner = math.floor(point[0])
        left = math.floor(degree/2)
        right = math.ceil(degree/2)

        if xcorner == point[0]: #then it is a gridpoint so we don't have any interpolation to do
            subs = np.zeros([1])
            subs[0] = self.values[xcorner]
            adjpoint = [point[0] - left]
            return subs, adjpoint
        else:
            xLower = xcorner-left
            xUpper = xcorner + right
            if xLower < 0:
                left = xcorner-0
                right = left+1
                xLower = 0
                xUpper = xcorner + right
                xwidth = 1
            if xUpper > self.values.shape[0]-1:
                xUpper = self.values.shape[0]-1
                right = xUpper-xcorner
                left = right-1
                xLower = xcorner-left
                ywidth = 1

            subs = np.zeros([xUpper-xLower+1])
            for i in range(xLower,xUpper+1):
                subs[i-xLower] = self.values[i]

            adjpoint = [point[0]-xcorner+left]
            #print(subs,adjpoint,left,right,xcorner)
            return subs,adjpoint
######################################################################################

    def _getSubValues2d(self,point, degree):
        floorX = int(math.floor(point[0]))
        floorY = int(math.floor(point[1]))
        half = math.floor(degree/2)
        fractionX = point[0]-floorX
        fractionY = point[1] - floorY
        cornerX = floorX-half
        cornerY = floorY - half
        length = degree + 1
        outofRange = False

        for i in range(cornerX,cornerX+length):
            for j in range(cornerY, cornerY+length):
                if i < 0:
                    outofRange = True
                if j < 0:
                    outofRange = True
                if i >= self.values.shape[0]:
                    outofRange = True
                if j >= self.values.shape[1]:
                    outofRange = True

        if outofRange:
            if degree > 1:
                return self._getSubValues2d(point,degree-1)
            else:
                subs = np.zeros([0])
                adjpoint = [0]

        else:
            subs = self.values[cornerX:cornerX + length,cornerY:cornerY + length]
            adjpoint = [half + fractionX, half + fractionY]

        return subs,adjpoint


