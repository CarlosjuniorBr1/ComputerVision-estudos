import cv2 
import mediapipe as mp
import time

#abre video ou webcam
cap = cv2.VideoCapture("myvideo.mp4")

mpHands = mp.solutions.hands
hands = mpHands.Hands()


while True: 
    sucess, img = cap.read()
    
    
    
    if not sucess:
        break
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()