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
    right(90)
    forward(3 * k)
    for j in range(2):
        left(90)
        forward(3 * k)
left(20)
for i in range(7):
    right(90)
    forward(3 * k)
    for j in range(2):
        left(90)
        forward(3 * k)

grid(-20, 20)

penup()
done()
