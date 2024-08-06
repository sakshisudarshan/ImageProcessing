import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('images.jpeg')
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,150,300)
kernel=np.ones((5,5),np.float32)/25
texture=cv2.filter2D(gray,-1,kernel)

plt.imshow(img1)
plt.show()
plt.imshow(edges)
plt.show()
plt.imshow(texture)
plt.show()
