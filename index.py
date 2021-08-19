from tkinter import *
from tkcalendar import *
from PIL import Image, ImageTk
from pygame import mixer

root = Tk()
root.title("Calendar")
root.geometry("425x685")
root.iconbitmap("D:/python projects/pythonProject/calculator/images.png")
root.resizable(False, False)
root.configure(background = "#1e747c")

img_1 = Image.open("Desert.jpg")
resize_1 = img_1.resize((400,400), Image.ANTIALIAS)
new_pic_1 = ImageTk.PhotoImage(resize_1)

img_2 = Image.open("Hydrangeas.jpg")
resize_2 = img_2.resize((400,400), Image.ANTIALIAS)
new_pic_2 = ImageTk.PhotoImage(resize_2)

img_3 = Image.open("Jellyfish.jpg")
resize_3 = img_3.resize((400,400), Image.ANTIALIAS)
new_pic_3 = ImageTk.PhotoImage(resize_3)

img_4 = Image.open("Koala.jpg")
resize_4 = img_4.resize((400,400), Image.ANTIALIAS)
new_pic_4 = ImageTk.PhotoImage(resize_4)

lab = Label(root)
lab.grid(row = 1, column = 1 ,pady = 20,padx = 10)
x = 1

def move ():
    global x
    if x == 4:
        x = 1
    if x == 1:
        lab.config(image = new_pic_1)
    elif x == 2:
        lab.config(image=new_pic_2)
    elif x == 3:
        lab.config(image=new_pic_3)
    elif x == 4:
        lab.config(image=new_pic_4)
    x+=1
    root.after(3000, move)
move()

cal = Calendar(root, selectmode="day", date_pattern="d/m/yy")
cal.grid(row = 2, column = 1, padx = 10, sticky = "nsew")

def play_music():
    mixer.init()
    mixer.music.load("2Pac Mama's Just A Little Girl.mp3")
    mixer.music.play(-1)

btn_play = Button(root, text = "Play sound", command = play_music)
btn_play.place(x = 30, y = 650)

global paused
paused = False

def pause_music(is_paused):
    global paused
    paused = is_paused

    if paused:
        mixer.music.unpause()
        paused =False
    else:
        mixer.music.pause()
        paused =True


btn_pause = Button(root, text = "Pause", command =lambda: pause_music(paused))
btn_pause.place(x = 185, y = 650)

def stop():
    mixer.music.stop()

btn_pause = Button(root, text = "stop sound", command = stop)
btn_pause.place(x = 310, y = 650)

root.mainloop()