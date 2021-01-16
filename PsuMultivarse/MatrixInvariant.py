'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --

singleton object to manage only loading pdbs once
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

'''
class MatrixInvariant:
    class __MatrixInvariant:
        def __init__(self):
            self.matrices = {}
        def __getMatrix__(self,dimensions):
            return self.matrices[self.strDim(dimensions)]
        def __existsMatrix__(self,dimensions):
            return self.strDim(dimensions) in self.matrices
        def __addMatrix__(self,dimensions,matrix):
            self.matrices[self.strDim(dimensions)] = matrix
        def strDim(self, dimensions):
            if len(dimensions) == 3:
                return str(dimensions[0]) + str(dimensions[1]) + str(dimensions[2])
            elif len(dimensions) == 2:
                return str(dimensions[0]) + str(dimensions[1])
            else:
                return str(dimensions[0])

    instance=None
    def __init__(self):
        if not MatrixInvariant.instance:
            MatrixInvariant.instance = MatrixInvariant.__MatrixInvariant()

    def getMatrix(self, dimensions):
        if self.instance.__existsMatrix__(dimensions):
            return self.instance.__getMatrix__(dimensions)
        else:
            matrix = self.createInvariantMatrix(dimensions)
            self.instance.__addMatrix__(dimensions, matrix)
            return matrix

    def createInvariantMatrix(self,dimensions):
        import numpy as np
        from numpy.linalg import inv
        import math
        dimX, dimY, dimZ = dimensions[0],1,1
        if len(dimensions) > 1:
            dimY = dimensions[1]
        if len(dimensions) > 2:
            dimZ = dimensions[2]

        simul = np.zeros([dimX*dimY*dimZ,dimX*dimY*dimZ])
        ser = -1
        for i in range(0, dimX):
            for j in range(0, dimY):
                for k in range(0, dimZ):
                    ser += 1
                    sec = -1
                    for ic in range(0, dimX):
                        for jc in range(0, dimY):
                            for kc in range(0, dimZ):
                                sec += 1
                                seCoeff = math.pow(i, ic) * math.pow(j, jc) * math.pow(k, kc);
                                simul[ser, sec] = seCoeff;

        invse = inv(simul)
        return invse


