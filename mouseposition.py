from tkinter import *
from pyautogui import position

def live_update():
   x['text'] = "X:" + str(position()[0])
   y['text'] = "Y:" + str(position()[1])
   win.after(1000, live_update)

win = Tk()

win.title("Mouse Position")
win.geometry('100x50')
win.attributes('-toolwindow', True)

x = Label(win, text ="")
x.place(x=10, y=10)

y = Label(win, text ="")
y.place(x=50, y=10)

live_update()
mainloop()
