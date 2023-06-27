import cv2

img = cv2.imread('girl.jpeg')
cv2.imwrite('save-girl.jpg',img)
cv2.waitKey(0)
