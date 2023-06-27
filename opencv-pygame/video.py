import cv2
import pygame

cap = cv2.VideoCapture(0)
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Face Detection")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    _,img = cap.read()
    faces = face_cascade.detectMultiScale(img,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f'x:{x},Y:{y}'
        cv2.putText(img,text,(x,y-10),font,0.5,(0,255,0),2)        
    cv2.imshow('img',img)
    img = pygame.surfarray.make_surface(img)
    screen.blit(img,(0,0))
    pygame.display.update()
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.quit()
