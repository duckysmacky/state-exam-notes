from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20

pendown()

def grid(w: int, h: int):
    penup()
    for x in range(w, h):
        for y in range(w, h):
            setpos(x * k, y * k)
            dot()

for i in range(4):
    for j in range(4):
        for n in range(4):
            forward(3 * k)
            right(60)
        forward(3 * k)
    forward(3 * k)

grid(-30, 30)

penup()
done()
