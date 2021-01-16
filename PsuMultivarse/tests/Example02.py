'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --
 A test file to try the MultiSolver
'''

import time
import numpy as np

from PsuMultivarse import MultiSolver as ms

def printTime(start,end,comment=''):
    time_diff = end - start
    timestring = str(int(time_diff/60)) + "m " + str(int(time_diff%60)) + "s"
    print(timestring,comment)


def makeUpSomeVals3d(dims):
    vals = np.zeros(dims)
    for i in range(0, dims[0]):
        for j in range(0, dims[1]):
            for k in range(0, dims[2]):
                vals[i,j,k] = i + j + k
    return vals

def makeUpSomeVals1d(dim):
    vals = np.zeros([dim])
    for i in range(0, dim):
            vals[i] = i^5*dim
    return vals


startx = time.time()
# make up some vals to shock the system
print('----------3d test----------')
for i in range(0,13):
    vals = makeUpSomeVals3d([i,i,i])
    solver = ms.MultiSolver(vals)
    ijk = int(i / 2)
    print(i, 'Val3d (1,1,1)',solver.getValue([1,1,1]),ijk*3,solver.getValue([ijk,ijk,ijk]))

print('----------1d test----------')
for i in range(0,22): # it loses ability to invert at 23
    vals = makeUpSomeVals1d(i)
    solver = ms.MultiSolver(vals)
    ijk = int(i / 2)
    print(i, 'Val1d (1)',solver.getValue([1]), ijk^5*i,solver.getValue([ijk]))

print('----------1d quadratic----------')
#A 1d quadratic
vals = np.zeros([3])
vals[0] = 1
vals[1] = 2
vals[2] = 7
solver = ms.MultiSolver(vals)
print('Vals at 0,0.5,1,1.5,2',solver.getValue([0]),solver.getValue([0.5]),solver.getValue([1]),solver.getValue([1.5]),solver.getValue([2]))

print('----------2d linear A----------')
#2 2d linear casea
vals = np.zeros([2,2])
vals[0,0] = 1
vals[0,1] = 1
vals[1,0] = 3
vals[1,1] = 5
solver = ms.MultiSolver(vals)
print('Val (0.5,0.5)',solver.getValue([0.5,0.5]))

print('----------2d linear B----------')
vals[0,0] = 11
vals[0,1] = 9
vals[1,0] = 15
vals[1,1] = 7
solver = ms.MultiSolver(vals)
print('val',solver.getValue([0.25,0.8]))
print('dv/dx',solver.getValueDx([0.25,0.8],1))
print('dv/dy',solver.getValueDy([0.25,0.8],1))

print('----------3d linear----------')
#A 3d linear casea
vals = np.zeros([2,2,2])
vals[0,0,0] = 1
vals[0,1,0] = 3
vals[1,0,0] = 3
vals[1,1,0] = 5
vals[0,0,1] = 3
vals[0,1,1] = 5
vals[1,0,1] = 5
vals[1,1,1] = 7
solver = ms.MultiSolver(vals)
print('Val (0.5,0.5,0.5)',solver.getValue([0.5,0.5,0.5]))

endx = time.time()
printTime(startx, endx)