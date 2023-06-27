import cv2
import numpy

img = cv2.imread('girl.jpeg')
print(img[0,0])
cv2.imshow('rgb',img)

b,g,r = cv2.split(img)
img1 = cv2.merge((g,b,r))
print(img1[0,0])
cv2.imshow('gbr',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
