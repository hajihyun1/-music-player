#mp3 재생 프로그램
from tkinter import *
from tkinter import filedialog
import os
import playsound
import webbrowser
#from pygame import mixer
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import sys


root= Tk()
root.title("mp3 재생 프로그램")
root.geometry("500x600+500+40")
root.resizable(False,False)

mp3_file_path="abc"

    
img1=PhotoImage(file="click.png")
label_img=Label(root, image=img1)
label_img.pack()

img2=PhotoImage(file="play.png")
label_img=Label(root, image=img2)
label_img.pack()
label_img.bind("<Button-1>", lambda e: play_sound(self=))

img3=PhotoImage(file="stop.png")
label_img=Label(root, image=img3)
label_img.pack()
label_img.bind("<Button-1>", lambda e: stop_sound())


def openfile():
    global filename
    filename = filedialog.askopenfilename(
        initialdir="C:/Users/Public",
        title="open file", 
        filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*"))
    )
    print(filename)
    webbrowser.open("Photograph.mp3")

def play_sound(self):
        file_path = "C:/Users/jihyu/Desktop/thinker/music player/Photograph.wav"  # 실제 MP3 파일 경로로 변경
        media_content = QMediaContent(QUrl.fromLocalFile(file_path))
        self.media_player.setMedia(media_content)
        self.media_player.setVolume(50)  # 볼륨 설정 (0~100)
        self.media_player.play()


def stop_sound():
    print(4234)

    
def click_img1(event):
    openfile()



# 윈도우에 마우스 클릭 이벤트 핸들러 등록
root.bind("<Button-2>", click_img1)  # <Button-1>은 왼쪽 버튼을 의미합니다
root.mainloop()