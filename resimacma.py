import cv2
import numpy as np
from matplotlib import pyplot as plt


resimGri = cv2.imread("foto.png")
resimGri = cv2.convertScaleAbs(resimGri,alpha=1.10,beta=40)
s = resimGri.shape

def Hist(image):
    H =np.zeros(shape=(256,1))
    s = image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            k= image[i,j]
            H[k,0] = H[k,0]+1
    return H
histg = Hist(resimGri)
plt.plot(histg)
plt.show()

x = histg.reshape(1,256)
y = np.zeros((1,256))
for i in range(256):
    if x[0,i] ==0:
        y[0,i]=0
    else:
        y[0,i] =i

min = np.min(y[np.nonzero(y)])
max = np.max(y[np.nonzero(y)])

stretch = np.round(((255-0)/(max-min))*(y-min))
stretch[stretch<0] = 0
stretch[stretch>255] =255

for i in range(s[0]):
    for j in range(s[1]):
        k =resimGri[i,j]
        resimGri[i,j] = stretch[0,k]

histg2 = Hist(resimGri)
cv2.imshow('germe',resimGri)
plt.plot(histg)
plt.plot(histg2)
plt.show()


# for i in range(len(histogram)-1) :
#     if histogram[i] != 0:
#         eskimin = histogram[i]
#         break

# for i in range(len(histogram)-1) :
#     if histogram[i] == 0:
#         eskimax = histogram[i-1]
#         break