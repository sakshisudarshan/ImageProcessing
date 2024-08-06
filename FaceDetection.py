import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('face.jpg')
haar_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
face_rect=haar_cascade.detectMultiScale(gray,1.1,9)
for (x,y,w,h) in face_rect :
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),8)
plt.imshow(img1)
plt.show()
