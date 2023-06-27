import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8)

cv2.line(img,(0,0),(100,100),(50,255,6),5)
cv2.circle(img,(100,100),50,(255,255,255),1)
cv2.rectangle(img,(200,200),(400,400),(60,55,255),10)
cv2.putText(img,'Hellow',(0,400),1,10,(255,0,1),1)

cv2.imshow('img',img[:,:,::-1])
cv2.waitKey(0)
