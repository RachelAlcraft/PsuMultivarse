'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --
 A test file to try the Interpolator
'''
import time
import numpy as np
import math
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
                #print('i,j=', vali, valj,solv,interpv)
                solvervals[ir,ic] = solv
                interpvals[ir, ic] = interpv
                linearvals[ir, ic] = linval
            ic += 1
    ir += 1

print(vals)
print(interpvals)
import matplotlib.pyplot as plt
plot1 = plt.figure(1)
plt.title('Multivariate square')
plt.imshow(solvervals,alpha=1)
plot2 = plt.figure(2)
plt.title('Interpolated square')
plt.imshow(interpvals)
plot3 = plt.figure(3)
plt.title('Interpolated linearly')
plt.imshow(linearvals)
plot4 = plt.figure(4)
plt.title('Original data')
plt.imshow(vals)


#------ Example with 5 degree interpolation
print('----------2d 5 degree ----------')
degree = 5
gaps = 20

vals2 = np.zeros([30,30])
vals2[8,8] = 1
vals2[9,9] = 1
vals2[9,10] = 1
vals2[10,10] = 2
vals2[11,11] = 4
vals2[12,11] = 3
vals2[10,11] = 4
vals2[10,11] = 5
vals2[11,10] = 4
vals2[20,20] = 2
vals2[21,21] = 4
vals2[22,21] = 8
vals2[20,21] = 4
vals2[20,21] = 5
vals2[21,20] = 1

vals2[14,14] = 6
vals2[14,15] = 6
vals2[14,16] = 6
vals2[16,16] = 6
vals2[15,14] = 6
vals2[15,15] = 10
vals2[15,16] = 10
vals2[15,17] = 6
vals2[16,13] = 6
vals2[16,14] = 6
vals2[16,17] = 6
vals2[16,16] = 10
vals2[16,15] = 10
vals2[17,17] = 6
vals2[18,17] = 6
vals2[17,14] = 6
vals2[17,15] = 3
vals2[17,16] = 2

vals2[4,14] = 6
vals2[4,15] = 6
vals2[4,16] = 6
vals2[6,16] = 6
vals2[5,14] = 6
vals2[5,15] = 10
vals2[5,16] = 10
vals2[5,17] = 6
vals2[6,14] = 6
vals2[6,17] = 6
vals2[6,16] = 10
vals2[6,15] = 10
vals2[7,17] = 6
vals2[8,17] = 6
vals2[7,14] = 6
vals2[7,15] = 6
vals2[7,16] = 6



print(vals2.shape)
rows=0
cols=0
for i in range(0,vals2.shape[0]*gaps):
    vali = i/gaps
    if vali <= vals2.shape[0]-1:
        rows = 0
        for j in range(0, vals2.shape[1]*gaps):
            valj = j / gaps
            if valj <= vals2.shape[1] -1:
                rows += 1
        cols += 1
print(rows,cols)

interpvals = np.zeros([rows,cols])
interp = ip.Interpolator(vals2)


ir = 0
for i in range(0,rows):
    vali = i/gaps
    if vali <= vals2.shape[0]-1:
        ic = 0
        for j in range(0, cols):
            valj = j / gaps
            if valj <= vals2.shape[1] -1:
                interpv = interp.getValue([vali,valj],degree)
                linval = interp.getValue([vali, valj], 1)
                solv = solver.getValue([vali,valj])
                interpvals[ir, ic] = interpv
            ic += 1
    ir += 1

plot5 = plt.figure(5)
plt.title('Interpolated 5 degree')
plt.imshow(interpvals)
plot6 = plt.figure(6)
plt.title('Original data')
plt.imshow(vals2)

#---------Show the data at the end

plt.show()


