'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --


 This script tests the MultiSolver class for accuracy. It shocks it to a large value to see where the numbers break down


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
            vals[i] = dim*i^5
    return vals


startx = time.time()
# make up some vals to shock the system
print('----------3d test----------')
for i in range(2,13): # breaks down in accuracy at 8
    vals = makeUpSomeVals3d([i,i,i])
    solver = ms.MultiSolver(vals)
    ijk = int(i / 2)
    print(i, 'Val3d (1,1,1)',':',solver.getValue([1,1,1]),' and ',ijk*3,':',solver.getValue([ijk,ijk,ijk]))

print('----------1d test----------')
for i in range(2,20): # it loses ability to invert at 23, breaks down in accuracy at 16
    vals = makeUpSomeVals1d(i)
    #print(vals)
    solver = ms.MultiSolver(vals)
    ijk = int(i / 2)
    print(i, 'Val1d',1*i^5,':',solver.getValue([1]), ' and ',i*ijk^5,':',solver.getValue([ijk]))

print('----------1d quadratic----------')
#A 1d quadratic
vals = np.zeros([3])
vals[0] = 1
vals[1] = 2
vals[2] = 7
solver = ms.MultiSolver(vals)
print('V=',solver.getPoly())
print('Vals at 0,0.5,1,1.5,2',solver.getValue([0]),solver.getValue([0.5]),solver.getValue([1]),solver.getValue([1.5]),solver.getValue([2]))

print('----------2d linear A----------')
#2 2d linear casea
vals = np.zeros([2,2])
vals[0,0] = 1
vals[0,1] = 1
vals[1,0] = 3
vals[1,1] = 5
solver = ms.MultiSolver(vals)
print('V=',solver.getPoly())
print('Val (0.5,0.5)',solver.getValue([0.5,0.5]))

print('----------2d linear B----------')
vals[0,0] = 11
vals[0,1] = 9
vals[1,0] = 15
vals[1,1] = 7
solver = ms.MultiSolver(vals)
print('V=',solver.getPoly())
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
print('V=',solver.getPoly())
print('Val (0.5,0.5,0.5)',solver.getValue([0.5,0.5,0.5]))
print('Val (0,0,0)',solver.getValue([0,0,0]))
print('Val (0,1,0)',solver.getValue([0,1,0]))
print('Val (1,1,1)',solver.getValue([1,1,1]))

print('----------Finished----------')
endx = time.time()
printTime(startx, endx)