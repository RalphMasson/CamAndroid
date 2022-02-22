import cv2
import numpy as np
url = 'http://192.168.1.81:8080/video'
path = r'C:\Users\MASSON\Desktop\Palm\img'
cap = cv2.VideoCapture(url)
i=0
while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

    if q == ord("c"):
        cv2.imwrite(path+"\\"+str(i)+"test.png",frame)
        i+=1
cv2.destroyAllWindows()
