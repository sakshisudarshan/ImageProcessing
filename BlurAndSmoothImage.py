import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('images.jpeg')
img2=cv2.blur(img1,(9,9))
img_smooth=cv2.bilateralFilter(img1,9,75,75)

plt.subplot(1,3,1)
plt.imshow(img1)
plt.subplot(1,3,2)
plt.imshow(img2)
plt.subplot(1,3,3)
plt.imshow(img_smooth)
plt.show()
