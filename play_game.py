# libraries
import cv2
import numpy as np
from random import randint

from keras import models
from keras.preprocessing import image
# initializing game points
bot = 0
you = 0
# selected area
LEFT, RIGHT, TOP, BOTTOM = (300, 600, 25, 325)

# defining the font
font = cv2.FONT_HERSHEY_COMPLEX
# function to generate opposition(Bot) gesture
def gen_opposition_gesture():
    return randint(0, 2)


# loading the model
model = models.load_model('model_RPS.hdf5')



def rps(match_number):

    opposition_gesture = gen_opposition_gesture()
    opposition_gesture = encoding(opposition_gesture)

    num_frames = 0
    global bot
    global you

    gesture = 'Waiting for 3 seconds'

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
            
            ret, read_screen = cap.read()
            read_screen = cv2.flip(read_screen,1)
            cv2.rectangle(read_screen, (LEFT, TOP), (RIGHT, BOTTOM), (150, 0, 0), 5)


            roi = read_screen[TOP:BOTTOM, LEFT:RIGHT]
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)

            ret, threshold = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            cv2.namedWindow("Area of Interest")
            cv2.moveWindow("Area of Interest", 1000, 200)
            cv2.imshow("Area of Interest", threshold)

            threshold = np.stack((threshold,) * 3, axis=-1)

            threshold_array = image.img_to_array(threshold)


            threshold_array = np.expand_dims(threshold_array, axis=0)

            if 40 <= num_frames < 100:

                pred = model.predict_classes(threshold_array)[0]

                gesture = encoding(pred)

            cv2.putText(read_screen, gesture, (10, 60), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

            if num_frames < 80:
                cv2.putText(read_screen, f'Welcome to RPS match number {match_number}', (5, 450), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                series = f"bot {bot} : You {you}"
                cv2.putText(read_screen, series, (10, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.imshow("Live Feed", read_screen)


            elif 80 <= num_frames < 100:
                cv2.putText(read_screen, 'Shooting!', (10, 450), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                series = f"bot {bot} : You {you}"
                cv2.putText(read_screen, series, (10, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.imshow("Live Feed", read_screen)

            elif num_frames == 100:
                if ((gesture == 'Rock' and opposition_gesture == 'Paper') or
                     (gesture == 'Scissor' and opposition_gesture == 'Rock') or
                     (gesture == 'Paper' and opposition_gesture == 'Scissor')
                ):
                    result_str = 'You lost this match'
                    bot+=1
                    
                elif gesture == opposition_gesture:
                    result_str = 'this match was Draw!'
                else:
                    result_str = 'You won this match'
                    you+=1
                    


            else:

                cv2.putText(read_screen, 'Opponent chose ' + opposition_gesture, (10, 350), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(read_screen, result_str, (10, 400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(read_screen, 'Press n to play next match', (10, 450), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                series = f"bot {bot} : You {you}"
                cv2.putText(read_screen, series, (10, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                

                

                if bot > you and match_number == 3:
                    cv2.putText(read_screen, f'you lost' , (10, 200), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.putText(read_screen, f'the series' , (10, 250), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.putText(read_screen,  series , (10, 300), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
                    
                elif bot == you and match_number == 3:
                    cv2.putText(read_screen, f'the series was' , (10, 200), font, 2, (0, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(read_screen, f'  a Draw' , (10, 250), font, 2, (0, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(read_screen,  series , (10, 300), font, 2, (0, 255, 255), 2, cv2.LINE_AA)
                elif bot < you and match_number == 3:
                    cv2.putText(read_screen, f'you won' , (10, 200), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.putText(read_screen, f'the series' , (10, 250), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.putText(read_screen,  series , (10, 300), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.imshow("Live Feed", read_screen)

           
            num_frames += 1

            
            key = cv2.waitKey(10)
            if key == 110:
                break


def encoding(encoding):
    switcher = {
        0: "Rock",
        1: "Paper",
        2: "Scissor",
    }

    return switcher.get(encoding, "nothing")


match_number = 1

while match_number < 4:
    rps(match_number)
    match_number+=1
if bot > you:
    print("you lost the series ")
elif bot == you:
    print("The series was a Draw")
else:
    print("you won the series ")
