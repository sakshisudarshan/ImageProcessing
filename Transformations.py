import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('images.jpeg')
rows,cols,_=img1.shape

M=np.float32([[1,0,100],[0,1,50]])
t_img=cv2.warpAffine(img1,M,(rows,cols))

h_img=cv2.resize(img1,(0,0),fx=0.5,fy=0.5)
d_img=cv2.resize(img1,(0,0),fx=2,fy=2)

cr=(rows/2,cols/2)
M=cv2.getRotationMatrix2D(cr,90,1)
r_img=cv2.warpAffine(img1,M,(rows+100,cols+100))

plt.subplot(1,4,1)
plt.imshow(t_img)
plt.subplot(1,4,2)
plt.imshow(h_img)
plt.subplot(1,4,3)
plt.imshow(d_img)
plt.subplot(1,4,4)
plt.imshow(r_img)
plt.show()
