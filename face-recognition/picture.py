import cv2

img = cv2.imread('warrior.jpeg')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(img,3,5)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('warrior',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
