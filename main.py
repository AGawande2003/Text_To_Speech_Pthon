import tkinter as tk
from tkinter import *
from tkinter import ttk
import pymysql
from gtts import gTTS
import pyttsx3

engine = pyttsx3.init()

top = tk.Tk()
top.config(bg="gg.png")
top.geometry("960x618")
c = Canvas(top, bg="gray16", height=618, width=690)
# bg =PhotoImage(file="bg.png")
# bgg=PhotoImage(file="file.png")
text = StringVar()
t = tk.Entry(top, font='Arial', bg="white", textvariable=text).place(x=180, y=150, width=600, height=200)
#text = tk.Entry(top, font='Arial', bg="white").place(x=100, y=150, width=600, height=200)
def speak():
    engine.setProperty('rate', 150)
    engine.say(text.get())
    engine.runAndWait()
    engine.stop()


def show():
    mydb = pymysql.connect(host="localhost", user="root", password="root", database="mydb")
    cur = mydb.cursor()
    cur.execute("SELECT id, Previous_recodings FROM userdata")
    global records
    records = cur.fetchall()
    disp()


def disp():
    root = tk.Tk()
    root.title("Recordings")
    label = tk.Label(root).grid(row=0, columnspan=3)
    cols = ('id', 'recodings')
    listBox = ttk.Treeview(root, columns=cols, show='headings')
    for i, (id, Previous_recodings) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, Previous_recodings))
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        closeButton = tk.Button(root, text="Close", width=15, command=root.destroy).grid(row=4, column=1)
    root.mainloop()


def save():
    mytext = t.get("text")
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("audio.mp3")
    mydb = pymysql.connect(host="localhost", user="root", password="root", database="mydb")
    cur = mydb.cursor()
    cur.execute("create database if not exists mydb")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Userdata(ID int AUTO_INCREMENT PRIMARY KEY,Previous_recodings varchar(255) NOT NULL)")
    sql = "insert into userdata(Previous_recodings)values(%s)"
    values = (mytext)
    cur.execute(sql, values)
    mydb.commit()


def exit():
    top.destroy()


im1=PhotoImage(file="play123.png")
im2=PhotoImage(file="poweroff123.png")
im3=PhotoImage(file="file.png")

title = ("                  Text To Speech Converter                  ")
b = tk.Button(top, text="Save", font="arial", bg="red", command=save).place(x=430, y=380, width=100, height=30)
b1 = tk.Button(top, compound=CENTER, image=im3, width=130, bg="black", padx=5, pady=5, command=show).place(x=230, y=450,width=100, height=100)
b2 = tk.Button(top, compound=CENTER, image=im1, width=130, bg="black", padx=5, pady=5, command=speak).place(x=430,
                                                                                                            y=450,
                                                                                                            width=100,
                                                                                                            height=100)
b3 = tk.Button(top, compound=CENTER, image=im2, width=130, bg="black", padx=5, pady=5, command=exit).place(x=630, y=450,
                                                                                                           width=100,
                                                                                                           height=100)
l1 = tk.Label(top, font=("BankGothic Md BT", '24', 'bold'), text=title, bg="lightcoral", fg="black").place(x=0, y=30,
                                                                                                           height=60)

top.mainloop()