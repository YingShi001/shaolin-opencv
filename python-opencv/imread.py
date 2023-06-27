import cv2

img = cv2.imread('girl.jpeg')
cv2.imshow('girl',img)
cv2.imwrite('save-girl.jpg',img)
cv2.waitKey(0)
cv2.destroyAllwindows()
