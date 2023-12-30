#mp3 재생 프로그램
from tkinter import *
from tkinter import filedialog
from pygame import *
import os
import playsound
import webbrowser
from pygame import mixer


root= Tk()
root.title("mp3 재생 프로그램")
root.geometry("500x600+500+40")
root.resizable(False,False)



filename=0
clicked=0
    
img1=PhotoImage(file="click.png")
label_img=Label(root, image=img1)
label_img.pack()

img2=PhotoImage(file="play.png")
label_img=Label(root, image=img2)
label_img.pack()
label_img.bind("<Button-1>", lambda e: play_sound())

img3=PhotoImage(file="stop.png")
label_img=Label(root, image=img3)
label_img.pack()

def openfile():
    global filename
    filename = filedialog.askopenfilename(
        initialdir="C:/Users/Public",
        title="open file", 
        filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*"))
    )
    print(filename)
    webbrowser.open("Photograph.mp3")

def play_sound():
    webbrowser.open("Photograph.mp3")


    
def click_img1(event):
    openfile()



# 윈도우에 마우스 클릭 이벤트 핸들러 등록
root.bind("<Button-2>", click_img1)  # <Button-1>은 왼쪽 버튼을 의미합니다
root.mainloop()