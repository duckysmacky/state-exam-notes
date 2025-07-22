from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20

left(90)
pendown()

def grid(w: int, h: int):
    penup()
    for x in range(w, h):
        for y in range(w, h):
            setpos(x * k, y * k)
            dot()

for i in range(7):
    forward(6 * k)
    right(270)

grid(-20, 20)

penup()
done()
