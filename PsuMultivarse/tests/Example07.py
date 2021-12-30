'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --


 This script loads the classic lena image from binary
 it performs a magnification for interpolation
 This is it can compare the method to the Thenenaz method
'''
import time
import numpy as np
import math
import matplotlib.pyplot as plt
from PsuMultivarse import Interpolator as ip
from PsuMultivarse import MultiSolver as ms

## User Input #################
###############################
degree = 9
###############################
#magnify eye
pixels, reduce, magnify, pixeloffset = 256,0.1,10,1200
pixels, reduce, magnify, pixeloffset = 256,0.05,20,2500

###############################

def loadImage(fileName):
    file = open(fileName, "rb")
    fileOrig = open(fileName, "rb")
    byte = file.read(1)
    i, j, = 0, 0
    pic = np.zeros((pixels, pixels))
    while byte:  # byte=false at end of file.
        val = int.from_bytes(byte, "big")
        pic[i, j] = val
        byte = file.read(1)
        j = j + 1
        if j >= pixels:
            j = 0
            i = i + 1
    file.close()
    return pic

# Code to load a real matrix of electron density data and visualise it with this library
vals = loadImage('lena.img')
interp = ip.Interpolator(vals)


rows = 0
cols = 0

pixelsWide = int(pixels*reduce*magnify)
pixelsHigh = int(pixels*reduce*magnify)

for i in range(0,pixelsWide):
    vali = i/magnify
    if vali <= vals.shape[0]-1:
        rows = 0
        for j in range(0, pixelsHigh):
            valj = j / magnify
            if valj <= vals.shape[1] -1:
                rows += 1
        cols += 1
print(rows,cols)

start = time.time()
solvervals = np.zeros([rows,cols])
solvervalslin = np.zeros([rows,cols])

ir = 0
for i in range(0,pixelsWide):
    vali = (i + pixeloffset)/magnify
    if vali <= vals.shape[0]-1:
        print(i, '/', rows)
        ic = 0
        for j in range(0, pixelsHigh):
            valj = (j + pixeloffset)/magnify
            if valj <= vals.shape[1] -1:
                solveropt = True

                if not solveropt:
                    solv = interp.getValue([vali,valj],degree)
                    solvlin = interp.getValue([vali, valj], 1)
                else:
                    subvals, adjpoint = interp.getSubValues([vali, valj], degree)
                    solver = ms.MultiSolver(subvals)
                    solv = solver.getValue(adjpoint)

                    subvalslin, adjpointlin = interp.getSubValues([vali, valj], 1)
                    solverlin = ms.MultiSolver(subvalslin)
                    solvlin = solverlin.getValue(adjpointlin)

                solvervals[ir,ic] = solv
                solvervalslin[ir, ic] = solvlin
            ic += 1
    ir += 1

plot = plt.figure(1)
plt.title('Multivariate linear interpolated function')
plt.imshow(solvervalslin,alpha=1, cmap='bone')

plot = plt.figure(2)
plt.title('Multivariate interpolated function,degree=' + str(degree))
plt.imshow(solvervals,alpha=1, cmap='bone')

plot = plt.figure(3)
plt.title('Multivariate Original Data')
plt.imshow(vals,alpha=1, cmap='bone')

end = time.time()
time_diff = end - start
timestring = str(int(time_diff / 60)) + "m " + str(int(time_diff % 60)) + "s"
print(timestring)

#---------Show the data at the end
plt.show()