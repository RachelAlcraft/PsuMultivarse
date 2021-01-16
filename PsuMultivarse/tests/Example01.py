'''
 -- ©Rachel Alcraft 2021, PsuMultivarse --
'''

import time

def printTime(start,end,comment=''):
    time_diff = end - start
    timestring = str(int(time_diff/60)) + "m " + str(int(time_diff%60)) + "s"
    print(timestring,comment)

from PsuMultivarse import MatrixInvariant as mi



# This test file simply gets lots of matrices :-)

#We do this twice to demonstrate the singleton pattern works

for go in range(0,2):
    minv = mi.MatrixInvariant()
    #Some 1d polynomials
    print('Polynomials',go)
    for i in range(0,15):
        start = time.time()
        mtx = minv.getMatrix([i, 1, 1])
        end = time.time()
        printTime(start, end,i)

    #some cubes
    print('Cubes', go)
    for i in range(0,15):
        start = time.time()
        mtx = minv.getMatrix([i, i, i])
        end = time.time()
        printTime(start, end,i)

minv = mi.MatrixInvariant()

#Tri-linear interpolation
mtx = minv.getMatrix([2, 2, 2])

# Spline
mtx = minv.getMatrix([4,1,1])
print(mtx)

# 5-degree 1d
mtx = minv.getMatrix([6,1,1])
print(mtx)

#Just something really big!
start = time.time()
mtx = minv.getMatrix([10,10,10])
print(mtx)
end = time.time()
printTime(start,end)
