import cv2
import mediapipe as mp
import pyautogui
from cvzone.HandTrackingModule import HandDetector
import speech_recognition as sr


hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0




def loop_b():

     _, frame = cap.read()
     frame = cv2.flip(frame, 1)
     frame_height, frame_width, _ = frame.shape
     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     output = hand_detector.process(rgb_frame)
     hands = output.multi_hand_landmarks
     if hands:
         for hand in hands:
             drawing_utils.draw_landmarks(frame, hand)
             landmarks = hand.landmark
             for id, landmark in enumerate(landmarks):
                 x = int(landmark.x*frame_width)
                 y = int(landmark.y*frame_height)


                 index_x = screen_width/frame_width*x
                 index_y = screen_height/frame_height*y

                 if id == 8:
                     cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                     thumb_x = screen_width/frame_width*x
                     thumb_y = screen_height/frame_height*y
                     print('outside', abs(index_y - thumb_y))
                     if abs(index_y - thumb_y) < 100:
                         pyautogui.moveTo(index_x, index_y)
     cv2.imshow('Virtual Mouse', frame)
     cv2.waitKey(1)





cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=2)


while True:

        ret, img = cap.read()
        hands, img = detector.findHands(img)



        if len(hands) == 1:

            if detector.fingersUp(hands[0]) == [0, 0, 0, 0, 0] or detector.fingersUp(hands[0]) == [1, 0, 0, 0, 0]:
                cv2.putText(img, "clique droit", (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 211), 12)
                print("clique droit")


            elif detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] or detector.fingersUp(hands[0]) == [1, 0, 0, 1, 0] or detector.fingersUp(hands[0]) == [0, 1,0 , 0, 0] or detector.fingersUp(hands[0]) == [0, 0, 0, 1, 0]:
                cv2.putText(img, "clique gauche", (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 211), 12)
                print("clique gauche")


            elif detector.fingersUp(hands[0]) == [1, 1, 1, 1, 1] or detector.fingersUp(hands[0]) == [0, 1, 1, 1, 1]:
                cv2.putText(img, "mouse", (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 211), 12)
                print("mouse")
                loop_b()


            else:
                cv2.putText(img, "nothing", (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 211), 12)
                print("nothing")

            # geste appris drag and drop, reload, get back, scroll, zoomer, dézoomer, speech

            #geste pour speech
            #import speech_recognition as sr

            #r = sr.Recognizer()
            #with sr.Microphone() as source:
                #print("Speak Anything :")
                #audio = r.listen(source)
                #try:
                    #text = r.recognize_google(audio)
                    #print("You said : {}".format(text))
                    #pyautogui.typewrite(text)
                #except:
                    #print("Sorry could not recognize what you said")


        cv2.imshow("Hand detector", img)

        if cv2.waitKey(1) and 0xFF == ord('c'):
            break


cap.release()
cv2.destroyAllWindows()
