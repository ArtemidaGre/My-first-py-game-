from tkinter import *
from os import *


main=Tk()
main.title('Запуск игры!)')
main.geometry('60x50')

def command1():
    startfile('data\Game.py')

text1=Label(main, text='Приятной игры!')
text1.grid(row=0, column=0)
button1=Button(main, text='Запустить!', command=command1)
button1.grid(row=1, column=0)

mainloop()
