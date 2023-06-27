import cv2

img = cv2.imread('girl.jpeg')
print(img.shape)
print(img.size)
print(img.dtype)
cv2.waitKey(0)
