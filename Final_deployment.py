from tensorflow import keras
import warnings
import numpy as np
import cv2
from googletrans import Translator
warnings.simplefilter(action='ignore', category=FutureWarning)
from tkinter import *
from PIL import Image, ImageDraw, ImageFont

lang=""
custom_font_path=""
word_dict=""
model=""

root = Tk()
root.geometry("1200x700")
root.title("Sign Language Translation")
root.config(bg="black")

def convert():
    global lang
    global custom_font_path
    lang=lang_var.get()
    if lang.lower()=="hindi":
        custom_font_path = 'Scripts\Hindi_Marathi.ttf'
        lang = 'hi'
    elif lang.lower()=="marathi":
        custom_font_path = 'Scripts\Hindi_Marathi.ttf'
        lang = 'mr'
    elif lang.lower()=="gujarati":
        custom_font_path = 'Scripts\Gujarati.ttf'
        lang = 'gu'
    elif lang.lower()=="kannada":
        custom_font_path = 'Scripts\Kannada.ttf'
        lang = 'kn'
    elif lang.lower()=="tamil":
        custom_font_path = 'Scripts\Tamil.ttf'
        lang = 'ta'
    elif lang.lower()=="telugu":
        custom_font_path = 'Scripts\Telugu.ttf'
        lang = 'te'
    elif lang.lower()=="bengali":
        custom_font_path = 'Scripts\Bangla.ttf'
        lang = 'bn'
    elif lang.lower()=="malayalam":
        custom_font_path = 'Scripts\Malayalam.ttf'
        lang = 'ml'
        
    return lang,custom_font_path

header_frame = Frame(root, bg='black', height=60)
header_frame.pack(fill=X, padx=10, pady=10)

header_label = Label(header_frame, text="Sign Language Translation", font="comicsans 40 bold", bg='black', fg="white")
header_label.pack(pady=10)

def on_language_selected(*args):
    selected_language = lang_var.get()
    print("Selected Language:", selected_language) 

languages = ["Hindi", "Gujarati", "Marathi", "Bengali", "Malayalam", "Telegu", "Tamil", "Kannada"] 

lang_var = StringVar(root)
lang_var.set("Select") 

language_dropdown = OptionMenu(root, lang_var, *languages)
language_dropdown.config(bg="black", fg="white", font="Arial 17")
language_dropdown.place(x=555,y=180)

lang_var.trace("w", on_language_selected)

text_label=Label(root, text="Enter your desired language", fg="white", font="comicsans 20 bold", bg="black")
text_label.place(x=425, y=120)

submit_button=Button(root, text="Submit", font="Arial 16", cursor="hand2", bg="black", fg="white", width=15, command=convert)
submit_button.config(width=10, height=1)
submit_button.place(x=550,y=280)


def overlay_text(frame, text, position, font_path, font_size, font_color):
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    try:
        custom_font = ImageFont.truetype(font_path, font_size)
        draw.text(position, text, fill=font_color, font=custom_font)
    except Exception as e:
        print("Error:", e)

    frame_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return frame_with_text

translator = Translator()

def translate_text(text, lang):
    translation = translator.translate(text, dest=lang)
    return translation.text

background = None
accumulated_weight = 0.5

ROI_top = 100
ROI_bottom = 300
ROI_right = 150
ROI_left = 350

def cal_accum_avg(frame, accumulated_weight):

    global background
    
    if background is None:
        background = frame.copy().astype("float")
        return None

    cv2.accumulateWeighted(frame, background, accumulated_weight)


def segment_hand(frame, threshold=25):
    global background
    
    diff = cv2.absdiff(background.astype("uint8"), frame)

    _, thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    
    contours, hierarchy = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None
    else:
        hand_segment_max_cont = max(contours, key=cv2.contourArea)

        return (thresholded, hand_segment_max_cont)

def camera():
    cam = cv2.VideoCapture(0)
    num_frames =0
    while True:
        ret, frame = cam.read()
    
        frame = cv2.flip(frame, 1)

        frame_copy = frame.copy()

        roi = frame[ROI_top:ROI_bottom, ROI_right:ROI_left]

        gray_frame = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)


        if num_frames < 70:
        
            cal_accum_avg(gray_frame, accumulated_weight)
        
            cv2.putText(frame_copy, "FETCHING BACKGROUND...PLEASE WAIT",
        (80, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
    
        else: 

            hand = segment_hand(gray_frame)

            if hand is not None:
            
                thresholded, hand_segment = hand

                cv2.drawContours(frame_copy, [hand_segment + (ROI_right,ROI_top)], -1, (255, 0, 0),1)
            
                cv2.imshow("Thesholded Hand Image", thresholded)
            
                thresholded = cv2.resize(thresholded, (64, 64))
                thresholded = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2RGB)
                thresholded = np.reshape(thresholded, (1, thresholded.shape[0], thresholded.shape[1], 3))
            
                pred = model.predict(thresholded)
                translated_text = translate_text(word_dict[np.argmax(pred)], lang)
                #cv2.putText(frame_copy, word_dict[np.argmax(pred)],(170, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                frame_copy = overlay_text(frame_copy, translated_text, (170, 45), custom_font_path, 40, (0, 0, 255))

            cv2.rectangle(frame_copy, (ROI_left, ROI_top), (ROI_right,ROI_bottom), (255,128,0), 3)

        num_frames += 1

        cv2.putText(frame_copy, "Sign Recognition", (10, 20), cv2.FONT_ITALIC, 0.5, (51,255,51), 1)
        cv2.imshow("Sign Detection", frame_copy)

        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

def handle_asl():
    global word_dict, model
    word_dict = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
    model = keras.models.load_model(r"Models/asl_model.h5")
    camera()

def handle_isl():
    global word_dict, model
    word_dict = {0:'One',1:'Two',2:'Three',3:'Four',4:'Five',5:'Six',6:'Seven',7:'Eight',8:'Nine'}
    model = keras.models.load_model(r"Models/isl_model.h5")
    camera()

def handle_gestures():
    global word_dict, model
    word_dict = {0: 'Bye', 1: 'Call Me', 2: 'Dislike', 3: 'Good Job', 4: 'Good Luck', 5: 'Peace', 6: 'Praying', 7: 'Rock On'}
    model = keras.models.load_model(r"Models/model.h5")
    camera()
    


asl_button=Button(root, text="American Sign Language", font="Arial 16", cursor="hand2", bg="black", fg="white", width=15, command=handle_asl)
asl_button.config(width=30, height=1)
asl_button.place(x=180,y=380)

isl_button=Button(root, text="Indian Sign Language", font="Arial 16", cursor="hand2", bg="black", fg="white", width=15, command=handle_isl)
isl_button.config(width=30, height=1)
isl_button.place(x=680,y=380)

ges_button=Button(root, text="Gestures", font="Arial 16", cursor="hand2", bg="black", fg="white", width=15, command=handle_gestures)
ges_button.config(width=10, height=1)
ges_button.place(x=550,y=480)


root.mainloop()