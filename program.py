import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

foto = cv2.imread("foto.png")

s = foto.shape # fotonun satır-sütun boyutlarını döndürür
def Hist(image): #histogram dönüştürücü fonk.
    H = np.zeros(shape=(256,1))#256 sütun, her sütun 1 satırlı, tüm değerler sıfır
    s = foto.shape # fotonun satır-sütun boyutlarını döndürür
    for i in range(s[0]): # s[0]satır
        for j in range(s[1]): #s[1] sütun
            k = image[i,j]
            H[k,0] = H[k,0]+1
    return H

H = Hist(foto)
plt.plot(H)

x = H.reshape(1,256)
y = np.array([])
y = np.append(y,x[0,0])

for i in range(255):
    k = x[0,i+1]+y[i]
    y = np.append(y,k)
y = np.round((y/(s[0]*s[1]))*255)

for i in range(s[0]):
    for j in range(s[1]):
        k = foto[i,j]
        foto[i,j] = y[k]
equal = Hist(foto)
plt.plot(equal)
plt.show()
