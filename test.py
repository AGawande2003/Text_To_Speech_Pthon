
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import scrolledtext
import pyttsx3


root = Tk()
root.title("")
root.geometry('600x480')
root.config(bg='salmon')
root.resizable()
info_label = Label(root, bg='purple', fg='white', bd=5, text="Enter Your Text Below", font="Georgia 28 bold")
info_label.grid(row=0, columnspan=3, padx=45, pady=10)


def speak():
    engine = pyttsx3.init()
    audio_string = my_text.get('0.0', END)
    if audio_string:
        engine.setProperty('rate', 180)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio_string)
        engine.runAndWait()
        engine.stop()


def save():
    engine = pyttsx3.init()
    audio_string = my_text.get('0.0', END)
    if audio_string:
        engine.setProperty('rate', 125)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.save_to_file(audio_string, 'sound.mp3')
        engine.runAndWait()
        engine.stop()

        result_label = Label(root, fg='white', bg='#63329f', font="arial 14 bold", bd=2,
                             text="File Saved as Sound.mp3")
        result_label.grid(row=3, columnspan=3, pady=4)


# my_text = scrolledtext(root, fg='#f00aba', bg='white', font="Verdana 12 bold", width=35, height=10, wrap=WORD,padx=10, pady=10, bd=5, relief=RIDGE)
my_text = scrolledtext()
my_text.grid(row=1, columnspan=3, pady=5)

speak_button = Button(root, fg='blue', bg='#0af0ba', text="Audio", font="arial 14 bold", bd=4, command=speak)
speak_button.grid(row=2, column=0, padx=5, pady=10)

save_button = Button(root, fg='blue', bg='#0af0ba', text="Convert and Save", font="arial 14 bold", bd=4, command=save)
save_button.grid(row=2, column=1, padx=5, pady=10)

clear_button = Button(root, fg='blue', bg='#0af0ba', text="Clear Text", font="arial 14 bold", bd=4,
                      command=lambda: my_text.delete('0.0', END))
clear_button.grid(row=2, column=2, padx=5, pady=10)

exit_button = Button(root, fg='blue', bg='#0af0ba', text="Exit", font="arial 14 bold", bd=4, command=lambda: my_msg())
exit_button.grid(row=2, column=3, padx=5, pady=10)


def my_msg():
    l2 = Label(root, text="ThankYou", bg='#63329f', fg='white', font="arial 14 bold", bd=2)
    l2.grid(row=4, columnspan=3, padx=5)
    root.after(1000, root.destroy)


root.mainloop()