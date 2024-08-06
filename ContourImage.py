import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('shapes.jpg')
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
edged= cv2.Canny(gray,30,200)
cont, hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print('number of contours found ='+str(len(cont)))
plt.imshow(img1)
plt.show()
plt.imshow(edged)
plt.show()
