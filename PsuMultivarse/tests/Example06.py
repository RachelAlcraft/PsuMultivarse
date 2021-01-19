'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --


 This script loads some real Electron Density data from 6JVV and
 finds the values and derivatives given different gaps and interpolating degrees

'''
import time
import numpy as np
import math
import matplotlib.pyplot as plt
from PsuMultivarse import Interpolator as ip
from PsuMultivarse import MultiSolver as ms

## User Input #################
###############################

gaps = 5
degree = 5

###############################

def loadSlice(filepath):
    with open(filepath, 'r') as f:
        ed_data = f.read().splitlines()

    rows = len(ed_data)
    ed_slice = np.zeros((rows, rows))
    for i in range(0, rows):
        row = ed_data[i].split(',')
        for j in range(0, rows):
            val = float(row[j])
            ed_slice[i, j] = val

    return ed_slice

# Code to load a real matrix of electron density data and visualise it with this library
vals = loadSlice('6jvv_slice.csv')
interp = ip.Interpolator(vals)


rows = 0
cols = 0

for i in range(0,vals.shape[0]*gaps):
    vali = i/gaps
    if vali <= vals.shape[0]-1:
        rows = 0
        for j in range(0, vals.shape[1]*gaps):
            valj = j / gaps
            if valj <= vals.shape[1] -1:
                rows += 1
        cols += 1
print(rows,cols)

start = time.time()
solvervals = np.zeros([rows,cols])
solvervals1d = np.zeros([rows,cols])
solvervals2d = np.zeros([rows,cols])
solvervals3d = np.zeros([rows,cols])

ir = 0
for i in range(0,rows):
    vali = i/gaps
    if vali <= vals.shape[0]-1:
        ic = 0
        for j in range(0, cols):
            valj = j / gaps
            if valj <= vals.shape[1] -1:

                solveropt = True

                if not solveropt:
                    solv = interp.getValue([vali,valj],degree)
                    solv1d = interp.getValueD([vali, valj],degree,1)
                    solv2d = interp.getValueD([vali, valj],degree, 2)
                    solv3d = interp.getValueD([vali, valj], degree, 3)
                else:
                    subvals, adjpoint = interp.getSubValues([vali, valj], degree)
                    solver = ms.MultiSolver(subvals)
                    solv = solver.getValue(adjpoint)
                    solv1d = solver.getValueD(adjpoint,1)
                    solv2d = solver.getValueD(adjpoint,2)
                    solv3d = solver.getValueD(adjpoint,3)

                solvervals[ir,ic] = solv
                solvervals1d[ir, ic] = solv1d
                solvervals2d[ir, ic] = solv2d
                solvervals3d[ir, ic] = solv3d

            ic += 1
    ir += 1

plot = plt.figure(1)
plt.title('Multivariate 3rd Derivative')
plt.imshow(solvervals3d,alpha=1)

plot = plt.figure(2)
plt.title('Multivariate 2nd Derivative')
plt.imshow(solvervals2d,alpha=1)

plot = plt.figure(3)
plt.title('Multivariate 1st Derivative')
plt.imshow(solvervals1d,alpha=1)

plot = plt.figure(4)
plt.title('Multivariate interpolated function')
plt.imshow(solvervals,alpha=1)

plot = plt.figure(5)
plt.title('Multivariate Original Data')
plt.imshow(vals,alpha=1)

end = time.time()
time_diff = end - start
timestring = str(int(time_diff / 60)) + "m " + str(int(time_diff % 60)) + "s"
print(timestring)

#---------Show the data at the end
plt.show()