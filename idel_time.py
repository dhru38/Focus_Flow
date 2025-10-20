import cv2
import activity
import time


faces_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detected (): 

    capture = cv2.VideoCapture(0)
    ret,img = capture.read()
    capture.release()

    if not ret  :
        return 0  # no frame captured 

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detected_faces = faces_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(30,30)
    )

    faces = len(detected_faces)
    if faces > 0 :
        activity.last_activity = time.time()
        return 1 
    return 0 

