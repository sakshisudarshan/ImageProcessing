import cv2
from matplotlib import pyplot as plt 

img1=cv2.imread('images.jpeg')
h,w,_=img1.shape
half=w//2
half2=h//2

lt=img1[:half,:half2]
rt= img1[:half,half2:]
lb=img1[half:,:half2]
rb=img1[half:,half2:]

plt.subplot(2,2,1)
plt.imshow(lt)
plt.subplot(2,2,2)
plt.imshow(rt)
plt.subplot(2,2,3)
plt.imshow(lb)
plt.subplot(2,2,4)
plt.imshow(rb)
plt.show()
