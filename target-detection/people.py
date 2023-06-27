import cv2

img = cv2.imread('people.png')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
(rects,weights) = hog.detectMultiScale(img,winStride=(4,4),padding=(8,8),scale=1.05)
for(x,y,w,h) in rects:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
