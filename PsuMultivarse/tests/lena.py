import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.image as mpimg
import numpy as np

'''
# This will simply display a picture
img = mpimg.imread('bluebell1.jpg')
imgplot = plt.imshow(img)
plt.show()
'''
files = []
files.append('C:/Dev/GithubExternal/interpol_thevenaz/Convolution/lena3.img')
files.append('C:/Dev/GithubExternal/interpol_thevenaz/Convolution/lena9.img')
files.append('lena.img')

plotidx = 1
for fileName in files:
    file = open(fileName, "rb")
    fileOrig = open(fileName, "rb")
    byte = file.read(1)
    i,j, = 0,0
    pic = np.zeros((256,256))
    while byte:# byte=false at end of file.
        val = int.from_bytes(byte, "big")
        pic[i,j] = val
        #print(val)
        byte = file.read(1)
        j = j+1
        if j >= 256:
            j = 0
            i = i+1
    print('dims=',i,j)
    file. close()
    plot = plt.figure(plotidx)

    title = "Lena Thevenaz "
    if plotidx == 1:
        title += ' 3 degrees'
    elif plotidx == 2:
        title += ' 9 degrees'
    else:
        title += ' original'

    plt.title(title, fontweight="bold")
    plt.imshow(pic, cmap='bone')
    plotidx += 1



#Save lena in my synthetic electron density format
'''
C,R,S,V
100,132,14,1E-15
101,132,14,1E-15
etc
'''


f = open("lena.syn", "w")
f.write('C,R,S,V\n')
for s in range(0,256):
    for i in range(0,256):
        for j in range(0, 256):
            f.write(str(i) + ',' + str(j) + ',' + str(s) + "," + str(pic[i, j]) + '\n')
            #f.write(str(i) + ',' + str(j) + ',' + str(s) + "," + str(100) + '\n')
f.close()

f = open("len2.syn", "w")
f.write('C,R,S,V\n')
for s in range(0,8):
    for i in range(0,128):
        for j in range(0, 128):
            f.write(str(i) + ',' + str(j) + ',' + str(s) + "," + str(pic[2*i, 2*j]) + '\n')
            #f.write(str(i) + ',' + str(j) + ',' + str(s) + "," + str(100) + '\n')

f = open("len2.syn", "w")
f.write('C,R,S,V\n')
for s in range(0,8):
    for i in range(0,12):
        for j in range(0, 12):
            f.write(str(i) + ',' + str(j) + ',' + str(s) + "," + str(pic[i, j]) + '\n')
            #f.write(str(i) + ',' + str(j) + ',' + str(s) + "," + str(100) + '\n')

f.close()

plt.show()