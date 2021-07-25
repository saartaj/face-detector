
import numpy as np 
import cv2
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()

while True:
    ret, frame= cap.read()
    frame = cv2.flip(frame, 1)

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= detector(gray)

    num=0
    for face in faces:
        x,y= face.left(), face.top()
        h,w= face.right(), face.bottom()
        cv2.rectangle(frame, (x,y), (h,w), (0,0,255),2)
        num += 1

        cv2.putText(frame, 'face '+str(num), (x-12, y-12), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255),2)

    cv2.imshow('faces', frame)
    k= cv2.waitKey()
    if k==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
