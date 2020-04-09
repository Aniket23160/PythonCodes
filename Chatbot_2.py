import speech_recognition as sr
import os
# import cv2
os.system('color 3f') # sets the background to blue

#make Python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")


# # # cam = cv2.VideoCapture(0)
# # cam .set(3,640)
# # cam.set(4,480)
# # face_detector = cv2.CascadeClassifier('/Users/DELL/Desktop/haarcascade_frontalface_default.xml')
# # face_id = input('\n enter user id end press <return> ==> ')
# # print("\n Intializing the Chatbot. Look the camera and wait ...for Access")
# speak.Speak('Intializing the Chatbot. Look the camera and wait ...for Access')


# count = 0
# while(True):
#     res, img = cam.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_detector.detectMultiScale(gray,1.3,5)
#     for(x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#         count+=1
#         #cv2.imwrite("dataset/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
#         cv2.imwrite("file://192.168.42.230/ImageData/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w]) 

#         cv2.imshow('image',img)
#     k=cv2.waitKey(100) & 0xff
#     if k==27:
#         break
#     elif count >=30:
#         break
# cam.release()
# cv2.destroyAllWindows()
# speak.Speak('face recognition successful')
speak.Speak('Please speak something')
r= sr.Recognizer()
with sr.Microphone() as source:
    print('Speak')
    audio = r.listen(source)
    text =r.recognize_google(audio)
    print('You said: {}'.format(text))
    # speak.Speak('{}'.r)
    # speak.Speak('Welcome to the World of A I  ')
    
