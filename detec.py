import cv2
import numpy as np
from face import  *
from trainne import *
#from tkinter import *

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.createLBPHFaceRecognizer()
rec.load('recognizer/trainner.yml')
global var1
var1=True
id=0

   
   
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 4)
while var1:
    ret, img =cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, 1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
        id, conf = rec.predict(gray[y:y+h,x:x+w])
        if (id==1):
            id=" shiwani"
        elif (id==2):
            id="Rishi"
        elif (id ==3):
           
            id=="santosh sir"
        
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
    cv2.imshow("Face",img);
       # if(id==1):
        #    id="Shiwani"
        #elif(id==2):
         #    id="Rishi"
   
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id), (x,y+h),font, 255)
    #cv2.imshow('Face',img) 
    if cv2.waitKey(1) ==ord('q'):
       break
    #var1=False
cam.release()
cv2.destroyAllWindows()


'''
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Good Bye'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side=BOTTOM)

root = Tk()
quitButton(root)

'''
