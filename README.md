# surf_with_hands


##This is a Python script that allows you to use your hand as a virtual mouse and perform different actions such as left click, right click and move the cursor using hand gestures. The script is built using the following libraries:

OpenCV - used for capturing and processing video frames.
Mediapipe - used for detecting and tracking hand landmarks.
PyAutoGUI - used for simulating mouse movement and clicks.
cvzone - used for detecting hand gestures.
SpeechRecognition - used for recognizing speech commands.


##Requirements:

Python 3.x
OpenCV
Mediapipe
PyAutoGUI
cvzone
SpeechRecognition


##How to use:

Clone the repository or download the zip file and extract it.
Install the required libraries using the command: pip install -r requirements.txt
Run the script using the command: python virtual_mouse.py
Place your hand in front of the camera and use the following gestures to perform different actions:
Fist: Right click
Index finger extended: Move the cursor
Thumb and index finger extended: Left click
All fingers extended: Enter mouse mode and use the index finger to move the cursor
Other gestures: Nothing happens


Note: To exit the script, press the 'c' key on the keyboard.

##Speech recognition:

The script also includes a feature to recognize speech commands. To use this feature, uncomment the following code in the script:

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        pyautogui.typewrite(text)
    except:
        print("Sorry could not recognize what you said")




![image](https://github.com/johannvig/surf_without_hands/assets/102874093/c499f5fd-5736-4659-aa93-077d05c27358)
