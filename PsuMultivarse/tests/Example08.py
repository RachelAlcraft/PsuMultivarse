'''
https://stackoverflow.com/questions/21885713/how-to-get-an-array-from-rgb-values-of-a-bitmap-image
https://www.dynamsoft.com/blog/insights/image-processing/image-processing-101-color-space-conversion/
'''
print("!!!")
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def loadImage(fileName):
    im = Image.open(fileName)
    im.load()
    pic = np.array(im)
    return pic
######################

NumPics = 100
FileDir = 'C:/Dev/Github/BbkProject/PhDThesis/3.Methods/3.AtomBlurImaging/Images1/'

vals = None
vals1d = None
vals2d = None
for i in range(0,NumPics):
    vals1 = loadImage(FileDir + 'tst ' + str(i) + '.bmp')
    w,h,d = vals1.shape
    print('new shape', i, w,h,d)
    if i == 0:
        vals = np.zeros((w, h))
        vals1d = np.zeros((w, h))
        vals2d = np.zeros((w, h))
    for i in range(0,w):
        for j in range(0, h):
            R = float(vals1[i,j,0])
            G = float(vals1[i,j,1])
            B = float(vals1[i,j,2])
            grey = 0.299*R + 0.587*G + 0.114*B
            greyscale = grey/NumPics
            vals[i, j] +=  greyscale



from PsuMultivarse import Interpolator as ip
from PsuMultivarse import MultiSolver as ms

interp = ip.Interpolator(vals)

w, h = vals.shape
print('Finding derivatives...')
for i in range(0, w):
    for j in range(0, h):
        print(i,j)
        vals1d[i,j] = interp.getValueD([i, j], 3, 1)
        vals2d[i, j] = interp.getValueD([i, j], 3, 2)

plot = plt.figure(1)
plt.title('Averaged Data')
plt.imshow(vals,alpha=1, cmap='bone')

plot = plt.figure(2)
plt.title('Averaged Data 1st Derivative')
plt.imshow(vals1d,alpha=1, cmap='inferno')

plot = plt.figure(3)
plt.title('Averaged Data 2nd Derivative')
plt.imshow(vals1d,alpha=1, cmap='jet')

#---------Show the data at the end
plt.show()