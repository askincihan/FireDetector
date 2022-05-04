
import cv2
from playsound import playsound
import pyaudio
import wave
import threading
import time
import subprocess
import os
import PIL.ImageGrab
from tkinter import *
import time
from PIL import ImageTk, Image
import pyautogui as pg





class FireDetector():  

    def __init__(self):

        self.open = True
        self.device_index = 0
        self.fps = 6               
        self.fourcc = "MJPG"        
        self.frameSize = (640,480)  
        self.video_filename = "fire_detected.avi"
        self.video_cap = cv2.VideoCapture(self.device_index)
        self.video_writer = cv2.VideoWriter_fourcc(*self.fourcc)
        self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
        self.frame_counts = 1
        self.start_time = time.time()

    def record(self):

        counter = 1
        timer_start = time.time()
        timer_current = 0


        while(self.open==True):
            ret, video_frame = self.video_cap.read()
            if (ret==True):

                    self.video_out.write(video_frame)
                    print(str(counter) + " " + str(self.frame_counts) + " frames written " + str(timer_current))
                    self.frame_counts += 1
                    counter += 1
                    timer_current = time.time() - timer_start
                    time.sleep(0.16)
                    gray = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow('video_frame', gray)
                    cv2.waitKey(1)
            else:
                break

    def stop(self):

        if self.open==True:

            self.open=False
            self.video_out.release()
            self.video_cap.release()
            cv2.destroyAllWindows()

        else: 
            pass


    # Launches the video recording function using a thread          
    def start(self):
        video_thread = threading.Thread(target=self.record)
        video_thread.start()



    def close1():
       win.quit()


   


    def start1():
        cap = cv2.VideoCapture(0)
        fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

        while(True):

        #    Flag = False  (For audio)

            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

            for (x,y,w,h) in fire: 
                Flag = True
                cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
                font = cv2.FONT_HERSHEY_COMPLEX    
                cv2.putText(frame,' FIRE!',(x-25,y-22),font,1,(220,20,60),1)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                print("Fire Detected!")

            cv2.imshow('frame', frame)

        #    if Flag == True:
        #        playsound('audio.mp3')
                
        #    else:
        #        pass

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            else:
                pass    





    


    win = Tk()


    win.geometry("400x200")

    Label(win, text="Fire Detector by askincihan", font=('Times New Roman', 12, 'bold')).pack(pady=10)

    button = Button(win, text="Dedektörü Başlat", font=('Aerial 11 bold'), background="#aa7bb1", foreground="white", command=start1)
    button.pack(pady=20)


    win.mainloop()

FireDetector()










######












