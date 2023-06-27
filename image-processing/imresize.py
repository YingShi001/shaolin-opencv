import cv2

img = cv2.imread('girl.jpeg')
img1 = cv2.imshow('girl-resize1',img[0:200,0:600])
img2 = cv2.imshow('girl-resize2',img[200:600,200:800])

cv2.waitKey(0)
cv2.destroyAllWindows()
