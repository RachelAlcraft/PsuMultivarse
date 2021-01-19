'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --


 This test file tries the interpolator class with a 1d and 2d made up polynomial sample


'''
import time
import numpy as np
import math
import matplotlib.pyplot as plt

from PsuMultivarse import Interpolator as ip
from PsuMultivarse import MultiSolver as ms

print('----------1d quadratic----------')
#A 1d quadratic that is v=2x^3-x
vals = np.zeros([6])
vals[0] = 0
vals[1] = 1
vals[2] = 14
vals[3] = 51
vals[4] = 124
vals[5] = 245
interp = ip.Interpolator(vals)
for i in range(0,11):
    val = i/2
    print('x=',val,'exp=',2*math.pow(val,3)-val,interp.getValue([val],3))
    #Note the interpolation is linear at the ends so only splined where there is space

print('----------2d linear ----------')
#2 2d linear casea
vals = np.zeros([6,6])
vals[0,0] = 1
vals[0,1] = 1
vals[0,2] = 1
vals[0,3] = 1
vals[1,0] = 5
vals[1,1] = 4
vals[1,2] = 5
vals[1,3] = 9
vals[2,0] = 2
vals[2,1] = 1
vals[2,2] = 1
vals[2,3] = 11
vals[3,0] = 6
vals[3,1] = 8
vals[3,2] = 9
vals[4,0] = 3
vals[4,1] = 4
vals[4,2] = 5
vals[3,3] = 11
vals[5,4] = 15
vals[5,5] = 12
interp = ip.Interpolator(vals)
solver = ms.MultiSolver(vals)

gaps = 30
degree = 3

rows = 0
cols = 0



for i in range(0,vals.shape[0]*gaps):
    vali = i/gaps
    if vali <= vals.shape[0]-1:
        rows = 0
        for j in range(0, vals.shape[1]*gaps):
            valj = j / gaps
            if valj <= vals.shape[1] -1:
                #print(vali,valj)
                rows += 1
        cols += 1
print(rows,cols)


solvervals = np.zeros([rows,cols])
solvervals1d = np.zeros([rows,cols])
interpvals = np.zeros([rows,cols])
linearvals = np.zeros([rows,cols])




ir = 0
for i in range(0,rows):
    vali = i/gaps
    if vali <= vals.shape[0]-1:
        ic = 0
        for j in range(0, cols):
            valj = j / gaps
            if valj <= vals.shape[1] -1:
                interpv = interp.getValue([vali,valj],degree)
                linval = interp.getValue([vali, valj], 1)
                solv = solver.getValue([vali,valj])
                solv1d = solver.getValueD([vali, valj],1)
                #print('i,j=', vali, valj,solv,interpv)
                solvervals[ir,ic] = solv
                solvervals1d[ir, ic] = solv1d
                interpvals[ir, ic] = interpv
                linearvals[ir, ic] = linval
            ic += 1
    ir += 1

print(vals)
print(interpvals)

plot1 = plt.figure(1)
plt.title('Multivariate square')
plt.imshow(solvervals,alpha=1)
plot1 = plt.figure(2)
plt.title('Multivariate first diff')
plt.imshow(solvervals1d,alpha=1)
plot2 = plt.figure(3)
plt.title('Interpolated square')
plt.imshow(interpvals)
plot3 = plt.figure(4)
plt.title('Interpolated linearly')
plt.imshow(linearvals)
plot4 = plt.figure(5)
plt.title('Original data')
plt.imshow(vals)


#---------Show the data at the end

plt.show()


