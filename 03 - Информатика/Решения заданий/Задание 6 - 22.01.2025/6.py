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

for i in range(6):
    forward(3 * k)
    right(300)
penup()
forward(3 * k)
right(270)
forward(2 * k)
right(90)
pendown()
for i in range(2):
    forward(3 * k)
    right(270)
    forward(4 * k)
    right(270)

grid(-20, 20)

penup()
done()
