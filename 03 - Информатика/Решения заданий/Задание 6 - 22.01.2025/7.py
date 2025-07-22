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

for i in range(4):
    forward(15 * k)
    right(90)
    forward(19 * k)
    right(90)
penup()
forward(8 * k)
right(90)
forward(6 * k)
left(90)
pendown()
for i in range(2):
    forward(89 * k)
    right(90)
    forward(77 * k)
    right(90)

grid(-20, 20)

penup()
done()
