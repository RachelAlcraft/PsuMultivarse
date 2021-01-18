'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --
This class fits a 12/2d/3d polynomial to the given values and returns the value of a partial derivative
 '''

import math
import numpy as np
from PsuMultivarse import MatrixInvariant as mi

class MultiSolver:

    def __init__(self,values):
        self.values = values
        minv = mi.MatrixInvariant()
        self.alcraft = minv.getMatrix(values.shape)
        self.dim = len(values.shape)
        self.shape = values.shape
        if self.dim == 3:
            self.vvalues = self._unwrapValues3d(values)
            coeffs = np.matmul(self.alcraft, self.vvalues)
            self.coeffs = self._unwrapCoeffs3d(coeffs)
        elif self.dim == 2:
            self.vvalues = self._unwrapValues2d(values)
            coeffs = np.matmul(self.alcraft, self.vvalues)
            self.coeffs = self._unwrapCoeffs2d(coeffs)
        else:
            self.vvalues = self._unwrapValues1d(values)
            coeffs = np.matmul(self.alcraft, self.vvalues)
            self.coeffs = self._unwrapCoeffs1d(coeffs)

    def getValue(self,point):
        if len(self.coeffs.shape) == 3:
            return round(self._getValue3d(point,self.coeffs),4);
        if len(self.coeffs.shape) == 2:
            return round(self._getValue2d(point,self.coeffs),4);
        else:
            return round(self._getValue1d(point,self.coeffs),4);

    def getPoly(self):
        if self.dim == 3:
            return self._getPoly3d()
        elif self.dim == 2:
            return self._getPoly2d()
        else:
            return self._getPoly1d()


    def getValueDx(self,point, diffs):
        vals = self.coeffs
        if len(self.coeffs.shape) == 3:
            for i in range(0, diffs):
                vals = self._diffWrtX3d(vals)
            return round(self._getValue3d(point,vals),4);
        if len(self.coeffs.shape) == 2:
            for i in range(0, diffs):
                vals = self._diffWrtX2d(vals)
            return round(self._getValue2d(point,vals),4);
        else:
            for i in range(0, diffs):
                vals = self._diffWrtX1d(vals)
            return round(self._getValue1d(point,vals),4);

    def getValueDy(self,point, diffs):#not 1d when y
        vals = self.coeffs
        if len(self.coeffs.shape) == 3:
            for i in range(0, diffs):
                vals = self._diffWrtY3d(vals)
            return round(self._getValue3d(point,vals),4);
        else:
            for i in range(0, diffs):
                vals = self._diffWrtY2d(vals)
            return round(self._getValue2d(point,vals),4);

    def getValueDz(self,point, diffs):#only 3d
        vals = self.coeffs
        for i in range(0, diffs):
            vals = self._diffWrtZ3d(vals)
        return round(self._getValue3d(point,vals),4);


    ##################################################################################
    #################Internal functions###########################################
    ##################################################################################
    def _getValue1d(self,point,coeffs):
        value = 0;
        for i in range(0,coeffs.shape[0]):
            coeff = coeffs[i];
            val = coeff * math.pow(point[0], i);
            value += val
        #print('2d', point, coeffs, value)
        return value

    def _getValue2d(self,point,coeffs):
        value = 0;
        for i in range(0,coeffs.shape[0]):
            for j in range(0,coeffs.shape[1]):
                coeff = coeffs[i, j];
                val = coeff * math.pow(point[0], i) * math.pow(point[1], j)
                value += val
        #print('2d',point,coeffs,value)
        return value

    def _getValue3d(self,point,coeffs):
        value = 0;
        for i in range(0,coeffs.shape[0]):
            for j in range(0,coeffs.shape[1]):
                for k in range(0,coeffs.shape[2]):
                    coeff = coeffs[i, j, k];
                    val = coeff * math.pow(point[0], i) * math.pow(point[1], j) * math.pow(point[2], k);
                    value += val;
        return value;


    def _unwrapValues1d(self,values):
        totallength = values.shape[0]
        vvalues = np.zeros([totallength])
        col = 0;
        for i in range(0,values.shape[0]):
            vvalues[col] = values[i]
            col = col+1
        return vvalues

    def _unwrapValues2d(self,values):
        totallength = values.shape[0]*values.shape[1]
        vvalues = np.zeros([totallength])
        col = 0;
        for i in range(0,values.shape[0]):
            for j in range(0,values.shape[1]):
                vvalues[col] = values[i, j]
                col = col+1

        return vvalues

    def _unwrapValues3d(self,values):
        totallength = values.shape[0]*values.shape[1]*values.shape[2]
        vvalues = np.zeros([totallength])
        col = 0;
        for i in range(0,values.shape[0]):
            for j in range(0,values.shape[1]):
                for k in range(0,values.shape[2]):
                    vvalues[col] = values[i, j, k]
                    col = col+1
        return vvalues


    def _unwrapCoeffs1d(self,CV):
        coeffs = np.zeros(self.shape)
        pos = 0;
        for i in range(0,self.shape[0]):
            coeffs[i] = CV[pos];
            pos = pos+1
        return coeffs

    def _unwrapCoeffs2d(self,CV):
        coeffs = np.zeros(self.shape)
        pos = 0;
        for i in range(0,self.shape[0]):
            for j in range(0,self.shape[1]):
                coeffs[i, j] = CV[pos];
                pos = pos+1
        return coeffs

    def _unwrapCoeffs3d(self,CV):
        coeffs = np.zeros(self.shape)
        pos = 0;
        for i in range(0,self.shape[0]):
            for j in range(0,self.shape[1]):
                for k in range(0,self.shape[2]):
                    coeffs[i, j, k] = CV[pos];
                    pos = pos+1
        return coeffs

    def _diffWrtX3d(self,coeffs):
        newcoeffs = np.zeros([coeffs.shape[0]-1,coeffs.shape[1],coeffs.shape[2]])
        for i in range(1,coeffs.shape[0]):
            for j in range(0,coeffs.shape[1]):
                for k in range(0,coeffs.shape[2]):
                    newcoeffs[i-1, j, k] = coeffs[i, j, k] * i;
        return newcoeffs;

    def _diffWrtX2d(self,coeffs):
        newcoeffs = np.zeros([coeffs.shape[0]-1,coeffs.shape[1]])
        for i in range(1,coeffs.shape[0]):
            for j in range(0,coeffs.shape[1]):
                newcoeffs[i-1, j] = coeffs[i, j] * i;
        return newcoeffs;

    def _diffWrtX1d(self,coeffs):
        newcoeffs = np.zeros([coeffs.shape[0]-1])
        for i in range(1,coeffs.shape[0]):
            newcoeffs[i-1] = coeffs[i] * i;
        return newcoeffs;

    def _diffWrtY3d(self, coeffs):
        newcoeffs = np.zeros([coeffs.shape[0], coeffs.shape[1]-1, coeffs.shape[2]])
        for i in range(0, coeffs.shape[0]):
            for j in range(1, coeffs.shape[1]):
                for k in range(0, coeffs.shape[2]):
                    newcoeffs[i,j-1, k] = coeffs[i, j, k] * j;
        return newcoeffs;

    def _diffWrtY2d(self, coeffs):
        newcoeffs = np.zeros([coeffs.shape[0],coeffs.shape[1]-1])
        for i in range(0, coeffs.shape[0]):
            for j in range(1, coeffs.shape[1]):
                newcoeffs[i,j-1] = coeffs[i, j] * j;
        return newcoeffs;

    def _diffWrtZ3d(self, coeffs):
        newcoeffs = np.zeros([coeffs.shape[0], coeffs.shape[1], coeffs.shape[2]-1])
        for i in range(0, coeffs.shape[0]):
            for j in range(0, coeffs.shape[1]):
                for k in range(1, coeffs.shape[2]):
                    newcoeffs[i,j, k-1] = coeffs[i, j, k] * k;
        return newcoeffs;

    def _getPoly3d(self):
        poly = ''
        for i in range(0, self.coeffs.shape[0]):
            for j in range(0, self.coeffs.shape[1]):
                for k in range(0, self.coeffs.shape[2]):
                    cf = self.coeffs[i,j,k]
                    if cf != 0:
                        if poly != '':
                            poly += ' + '
                        poly += str(self.coeffs[i,j,k])
                        if i > 0:
                            poly += 'x'
                            if i > 1:
                                poly += '^' + str(i)
                        if j > 0:
                            poly += 'y'
                            if j > 1:
                                poly += '^' + str(j)
                        if k > 0:
                            poly += 'z'
                            if j > 1:
                                poly += '^' + str(k)

        return poly;

    def _getPoly2d(self):
        poly = ''
        for i in range(0, self.coeffs.shape[0]):
            for j in range(0, self.coeffs.shape[1]):
                cf = self.coeffs[i,j]
                if cf != 0:
                    if poly != '':
                        poly += ' + '
                    poly += str(self.coeffs[i,j])
                    if i > 0:
                        poly += 'x'
                        if i > 1:
                            poly += '^' + str(i)
                    if j > 0:
                        poly += 'y'
                        if j > 1:
                            poly += '^' + str(j)

        return poly;

    def _getPoly1d(self):
        poly = ''
        for i in range(0, self.coeffs.shape[0]):
            cf = self.coeffs[i]
            if cf != 0:
                if poly != '':
                    poly += ' + '
                poly += str(self.coeffs[i])
                if i > 0:
                    poly += 'x'
                    if i > 1:
                        poly += '^' + str(i)

        return poly;






