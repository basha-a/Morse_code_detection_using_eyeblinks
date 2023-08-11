# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

#-----Use VideoCapture in OpenCV-----
import cv2
import dlib
import math

# creates a Tk() object
master = Tk()
 
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	# Dictionary representing the morse code chart
	MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

	cipher = ''
	for letter in message:
		if letter != ' ':
			# Looks up the dictionary and adds the
			# corresponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += '  '
	return cipher

# Hard-coded driver function to run the program

# sets the geometry of main
# root window
master.geometry("700x350")
master.title('MORSE CODE')
def open_decode():
    BLINK_RATIO_THRESHOLD = 5.4

    def dataset(c):
        morseDict={
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        '.-.-': ' '
        }

        if morseDict.get(c)!='Check':
            return (morseDict.get(c))
        else: 
            return ''

    def converter(s):
        code=s.split()
        message=''    
        for c in code:
            message+=dataset(c)
            message+=' '
        return message

    def midpoint(point1 ,point2):
        return int((point1.x + point2.x)/2), int((point1.y + point2.y)/2)

    def euclidean_distance(point1 , point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


    def get_blink_ratio(eye_points, facial_landmarks):
    
    #loading all the required points
        corner_left  = (facial_landmarks.part(eye_points[0]).x, 
                        facial_landmarks.part(eye_points[0]).y)
        corner_right = (facial_landmarks.part(eye_points[3]).x, 
                        facial_landmarks.part(eye_points[3]).y)
    
        center_top    = midpoint(facial_landmarks.part(eye_points[1]), 
                                 facial_landmarks.part(eye_points[2]))
        center_bottom = midpoint(facial_landmarks.part(eye_points[5]), 
                                 facial_landmarks.part(eye_points[4]))

        #calculating distance
        horizontal_length = euclidean_distance(corner_left,corner_right)
        vertical_length = euclidean_distance(center_top,center_bottom)

        ratio = horizontal_length / vertical_length

        return ratio

    #-----livestream from the webcam----- 
    cap = cv2.VideoCapture(0)

    '''in case of a video
    cap = cv2.VideoCapture("__path_of_the_video__")'''

    #-----name of the display window in OpenCV-----
    cv2.namedWindow('DECODE')

    #-----Face detection with dlib-----
    detector = dlib.get_frontal_face_detector()

    #-----Detecting Eyes using landmarks in dlib-----
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    #-----these landmarks are based on the image above-----
    left_eye_landmarks  = [36, 37, 38, 39, 40, 41]
    right_eye_landmarks = [42, 43, 44, 45, 46, 47]

    flag=0
    s=''
    duration=''

    while True:
        #-----capturing frame-----
        retval, frame = cap.read()

        #-----exit the application if frame not found-----
        if not retval:
            print("Can't receive frame (stream end?). Exiting ...")
            break 

        #-----converting image to grayscale-----
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #-----Face detection with dlib-----
        #detecting faces in the frame 
        faces,_,_ = detector.run(image = frame, upsample_num_times = 0, 
                           adjust_threshold = 0.0)

        #-----Detecting Eyes using landmarks in dlib-----
        for face in faces:
        
            landmarks = predictor(frame, face)

            #-----Calculating blink ratio for one eye-----
            left_eye_ratio  = get_blink_ratio(left_eye_landmarks, landmarks)
            right_eye_ratio = get_blink_ratio(right_eye_landmarks, landmarks)
            blink_ratio     = (left_eye_ratio + right_eye_ratio) / 2
        
            if blink_ratio > BLINK_RATIO_THRESHOLD:
            #-----Blink detected!-----
                fl=f'{flag}'
                cv2.putText(frame,fl,(10,50), cv2.FONT_HERSHEY_SIMPLEX,
                           2,(255,255,255),2,cv2.LINE_AA)
                flag+=1
            else: 
                #-----detect if dot or dash-----
                if flag>1 and flag<8:
                    s+='.'                
                if flag>8 and flag<=20:
                    s+='-' 
                if flag>20 and flag<=100:
                    s+=' '
                flag=0
        
            cv2.putText(frame,s,(10,100), cv2.FONT_HERSHEY_SIMPLEX,
                            2,(255,255,255),2,cv2.LINE_AA)
            cv2.putText(frame,converter(s),(10,150), cv2.FONT_HERSHEY_SIMPLEX,
                            2,(255,255,255),2,cv2.LINE_AA)

        cv2.imshow('DECODE', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    #-----releasing the VideoCapture object-----
    cap.release()
    cv2.destroyAllWindows()

# function to open a new window
# on a button click
def openNewWindow():
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        
        lbl.config(text = encrypt(inp.upper()),font=("Arial", 25))

    # Toplevel object which will
    # be treated as a new window
    frame = Toplevel(master)
    frame.title('ENCODE')
    # sets the title of the
    # Toplevel widget
    frame.title("New Window")
 
    # sets the geometry of toplevel
    frame.geometry("700x350")
 
    # A Label widget to show in toplevel
    # TextBox Creation
    inputtxt = Text(frame,
                   height = 2,
                   width = 50)
    inputtxt.pack(pady = 50)
  
    # Button Creation
    printButton = Button(frame,
                        text = "GENERATE MORSE CODE", 
                        command = printInput)
    printButton.pack(pady = 30)
  
    # Label Creation
    lbl = Label(frame, text = "")
    lbl.pack()
    frame.mainloop()
 
 
 
# a button widget which will open a
# new window on button click

btn = Button(master,
             text ="\n\n\nENCODE\n\n\n",
             width=30,
             command = openNewWindow)
btn.pack(pady = 20)

btn = Button(master,
             text ="\n\n\nDECODE\n\n\n",
             width=30,
             command = open_decode)
btn.pack(pady = 20)


 
# mainloop, runs infinitely
mainloop()