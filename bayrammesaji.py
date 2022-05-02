from tkinter.ttk import Style
import turtle
from turtle import *
ekran=Screen()
ekran.bgcolor('black')

t=turtle.Turtle()
t.pencolor('white')

def kalip():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def kalp_olustur():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    kalip()
    t.lt(120)
    kalip()
    t.fd(112)
    t.end_fill() 
kalp_olustur()
t.ht()


def yazdırma_fonk(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style=('Stencil Std',18,'italic')
    t.write(message,font=(style))

yazdırma_fonk('İ',(-75,95))
yazdırma_fonk('Y',(-70,95))
yazdırma_fonk('İ',(-55,95))
yazdırma_fonk('B',(-40,95))
yazdırma_fonk('A',(-25,95))
yazdırma_fonk('Y',(-10,95))
yazdırma_fonk('R',(5,95))
yazdırma_fonk('A',(20,95))
yazdırma_fonk('M',(35,95))
yazdırma_fonk('L',(55,95))
yazdırma_fonk('A',(65,95))
yazdırma_fonk('R',(80,95))



ekran.mainloop()