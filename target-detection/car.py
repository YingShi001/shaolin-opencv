import cv2

img = cv2.imread('car.jpg')
car_cascade = cv2.CascadeClassifier('cars.xml')
cars = car_cascade.detectMultiScale(img,1.1,3)
for(x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
