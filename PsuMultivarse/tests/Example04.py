'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --


 This test file tries the interpolator for visualisation in 2d
 It tries out differentiation up to 3rd


'''
import time
import numpy as np
import math
import matplotlib.pyplot as plt

from PsuMultivarse import Interpolator as ip
from PsuMultivarse import MultiSolver as ms

#------ Example with 5 degree interpolation
print('----------2d 5 degree ----------')
degree = 5
gaps = 10

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
splintvals = np.zeros([rows,cols])
linearvals = np.zeros([rows,cols])

interpvalsd = np.zeros([rows,cols])
splintvalsd = np.zeros([rows,cols])
lineard = np.zeros([rows,cols])

interp = ip.Interpolator(vals2)


ir = 0
for i in range(0,rows):
    vali = i/gaps
    if vali <= vals2.shape[0]-1:
        ic = 0
        for j in range(0, cols):
            valj = j / gaps
            if valj <= vals2.shape[1] -1:
                interpv = interp.getValue([vali,valj],5)
                splval = interp.getValue([vali, valj], 3)
                linval = interp.getValue([vali, valj], 1)
                interpvals[ir, ic] = interpv
                linearvals[ir, ic] = linval
                splintvals[ir, ic] = splval
                #derivatives
                interpv = interp.getValueD([vali, valj], 5,1)
                splval = interp.getValueD([vali, valj], 3,1)
                lind = interp.getValueD([vali, valj], 1, 1)
                interpvalsd[ir, ic] = interpv
                splintvalsd[ir, ic] = splval
                lineard[ir, ic] = lind

            ic += 1
    ir += 1

plot5 = plt.figure(1)
plt.title('Interpolated 5 degree')
plt.imshow(interpvals)
plot6 = plt.figure(2)
plt.title('Interpolated 3 degree')
plt.imshow(splintvals)
plot7 = plt.figure(3)
plt.title('Interpolated linear')
plt.imshow(linearvals)
plot8 = plt.figure(4)
plt.title('Original data')
plt.imshow(vals2)
plot8 = plt.figure(9)
plt.title('Deriv 1')
plt.imshow(lineard)
plot = plt.figure(10)
plt.title('Deriv 3')
plt.imshow(splintvalsd)
plot = plt.figure(11)
plt.title('Deriv 5')
plt.imshow(interpvalsd)

#---------Show the data at the end

plt.show()


