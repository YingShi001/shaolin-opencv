import cv2

img = cv2.imread('girl.jpeg')

img1 = cv2.imread('girl.jpeg',0)
img1 = cv2.imshow('gril-gray',img1)

img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img2 = cv2.imshow('girl-hsv',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
