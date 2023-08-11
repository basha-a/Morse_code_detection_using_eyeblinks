									MORSE CODE DETECTION USING EYE BLINKS
				
	This project aims to detect and interpret Morse code messages using eye blinks. The system utilizes computer vision techniques to track eye movements and interpret the blinking patterns as Morse code signals. The implementation is based on the assumption that a person blinks intentionally to communicate Morse code.
 
SETUP AND DEPENDENCIES :-

To run this project, you will need the following dependencies:

 --> Python (version 3.7 or higher)
 --> OpenCV (Open Source Computer Vision Library)
 --> NumPy (Numerical Python)
 --> Dlib (A toolkit for making real-world machine learning and data analysis applications)
 --> SciPy (Scientific Python library)
 --> Imutils (A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization
     and displaying Matplotlib images easier)
 
HOW IT WORKS :-

 --> The system captures video frames from the webcam.
 --> Face detection is performed using Haar cascades or deep learning-based methods to locate the face region in the frame.
 --> Facial landmarks are detected using the Dlib library to identify the eye regions.
 --> The eye aspect ratio (EAR) is calculated to determine if the eyes are open or closed.
 --> A blink is detected when the EAR drops below a certain threshold, indicating a closed eye.
 --> Blink duration and time intervals between blinks are measured to interpret them as dots, dashes, and spaces in Morse code.
 --> The Morse code signals are decoded using a lookup table to convert them into alphanumeric characters.
 --> The decoded messages are displayed in the terminal.

HOW TO USE :-

 --> Run the "maincode.py" file using python.
 --> It will show Encode and Decode option.
 --> If you select Encode the given english words or letter is converted into Morse code.
 --> If you select Decode the system will use your webcam to detect and track your eye blinks.
 --> Blink intentionally to send Morse code signals.
 --> The detected Morse code messages will be displayed in the terminal.

CONCLUSION :-

	The Morse code detection system using eye blinks provides a unique way to communicate Morse code messages through intentional blinking. By leveraging computer vision techniques, the system enables users to send messages using eye blinks, opening up possibilities for alternative communication methods.