'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --


 This is a test file to invedtigate how large a lultovariate fit can get before accuracy is lost
 It seems to be degree 5 is ok but not thereafter

'''
import time
import numpy as np
import math
import matplotlib.pyplot as plt
from PsuMultivarse import MultiSolver as ms

def printTime(start,end,comment=''):
    time_diff = end - start
    timestring = str(int(time_diff/60)) + "m " + str(int(time_diff%60)) + "s"
    print(timestring,comment)

#3 and 5 work but it breaks down at 7
size = 5
gaps = 20


print('----------2d linear ----------')
#2 2d linear casea
vals = np.zeros([size+1,size+1])
centre = int(size/2)

vals[centre-1,centre-1] = 4
vals[centre-1,centre] = 4
vals[centre-1,centre+1] = 3
vals[centre-1,centre] = 3
vals[centre,centre] = 8
vals[centre,centre+1] = 6
vals[centre+1,centre-1] = 4
vals[centre+1,centre] = 4
vals[centre+1,centre+1] = 3

vals[0,0] = 4
vals[0,1] = 4
vals[1,1] = 3
vals[2,1] = 3

solver = ms.MultiSolver(vals)
poly = 'V=' + solver.getPoly()

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

ir = 0
for i in range(0,rows):
    vali = i/gaps
    if vali <= vals.shape[0]-1:
        ic = 0
        for j in range(0, cols):
            valj = j / gaps
            if valj <= vals.shape[1] -1:
                solv = solver.getValue([vali,valj])
                solv1d = solver.getValueD([vali, valj],1)
                solv2d = solver.getValueD([vali, valj], 2)

                solvervals[ir,ic] = solv
                solvervals1d[ir, ic] = solv1d
                solvervals2d[ir, ic] = solv2d

            ic += 1
    ir += 1


plot = plt.figure(1)
plt.title('Multivariate 2nd Derivative')
plt.imshow(solvervals2d,alpha=1)

plot = plt.figure(2)
plt.title('Multivariate 1st Derivative')
plt.imshow(solvervals1d,alpha=1)

plot = plt.figure(3)
plt.title('Multivariate interpolated function')
plt.imshow(solvervals,alpha=1)

plot = plt.figure(4)
plt.title('Multivariate Original Data')
plt.imshow(vals,alpha=1)

print(poly)

end = time.time()
printTime(start,end)

#---------Show the data at the end
plt.show()


