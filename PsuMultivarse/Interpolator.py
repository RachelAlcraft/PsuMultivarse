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


    def getSubValues(self,point, degree):
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
            return subvalues, adjpoint

        return 0

    def getValue(self,point, degree):
        '''
        :param point: the [x] or [x,y] or [x,y,z] tuple
        :param degree: the polynomial fit degree, must be an odd number, 1 is linear, 3 is spline etc
        :return: the interpolated value
        '''
        subvals,adjpoint = self.getSubValues(point,degree)
        solver = ms.MultiSolver(subvals)
        return solver.getValue(adjpoint)


    def getValueD(self,point, degree, diffs):
        '''
        :param point: the [x] or [x,y] or [x,y,z] tuple
        :param degree: the polynomial fit degree, must be an odd number, 1 is linear, 3 is spline etc
        :return: the interpolated value
        '''
        subvals, adjpoint = self.getSubValues(point, degree)
        solver = ms.MultiSolver(subvals)
        return solver.getValueD(adjpoint,diffs)

    def getSlice(self, points, width,gaps):
        '''
        This returns a 2d slice of points where the centre is given and for 2d a linear point is also given, for 3d a planary point is also neeed.
        The square is drawn around these points and then interpolated at the specified gap. Note it need not be orthogonal to the axes.
        :param points:
        :param width:
        :param gaps:
        :return:
        '''
        return 0


    #####################################################################
    ###### Internal Functions #########################################
    #####################################################################

    def _getSubValues1d(self,point, degree):
        floorX = int(math.floor(point[0]))
        half = math.floor(degree / 2)
        fractionX = point[0] - floorX
        cornerX = floorX - half
        length = degree + 1
        outofRange = False

        for i in range(cornerX, cornerX + length):
            if i < 0:
                outofRange = True
            if i >= self.values.shape[0]:
                outofRange = True

        if outofRange:
            if degree > 1:
                return self._getSubValues1d(point, degree - 1)
            else:
                subs = np.zeros([0])
                adjpoint = [0]

        else:
            subs = self.values[cornerX:cornerX + length]
            adjpoint = [half + fractionX]

        return subs, adjpoint

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


    def _getSubValues3d(self,point, degree):
        floorX = int(math.floor(point[0]))
        floorY = int(math.floor(point[1]))
        floorZ = int(math.floor(point[2]))
        half = math.floor(degree/2)
        fractionX = point[0]-floorX
        fractionY = point[1] - floorY
        fractionZ = point[2] - floorZ
        cornerX = floorX-half
        cornerY = floorY - half
        cornerZ = floorZ - half
        length = degree + 1
        outofRange = False

        for i in range(cornerX,cornerX+length):
            for j in range(cornerY, cornerY+length):
                for k in range(cornerZ, cornerZ + length):
                    if i < 0:
                        outofRange = True
                    if j < 0:
                        outofRange = True
                    if k < 0:
                        outofRange = True
                    if i >= self.values.shape[0]:
                        outofRange = True
                    if j >= self.values.shape[1]:
                        outofRange = True
                    if k >= self.values.shape[2]:
                        outofRange = True

        if outofRange:
            if degree > 1:
                return self._getSubValues3d(point,degree-1)
            else:
                subs = np.zeros([0])
                adjpoint = [0]
        else:
            subs = self.values[cornerX:cornerX + length,cornerY:cornerY + length,cornerZ:cornerZ + length]
            adjpoint = [half + fractionX, half + fractionY, half + fractionZ]

        return subs,adjpoint


