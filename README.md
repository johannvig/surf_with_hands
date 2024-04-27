# surf_with_hands

## Description

Surf With Hands is a Python script that transforms your hand into a virtual mouse, allowing you to use hand gestures to control your computer's cursor and perform various actions like clicking and moving. This script leverages multiple libraries for video capture, hand landmark detection, mouse control simulation and even speech recognition for voice commands.

- **OpenCV**: Capturing and processing video frames.
- **Mediapipe**: Detecting and tracking hand landmarks.
- **PyAutoGUI**: Simulating mouse movements and clicks.
- **cvzone**: Detecting hand gestures.
- **SpeechRecognition**: Recognizing speech commands.

## Requirements
- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI
- cvzone
- SpeechRecognition


## How to use:

Place your hand in front of the camera and use the following gestures to perform different actions:
Fist: Right click
Index finger extended: Move the cursor
Thumb and index finger extended: Left click
All fingers extended: Enter mouse mode and use the index finger to move the cursor
Other gestures: Nothing happens


Note: To exit the script, press the 'c' key on the keyboard.

## Speech recognition:

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
