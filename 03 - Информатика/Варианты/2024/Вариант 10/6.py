from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20

def grid(w, h):
    for x in range(-w, w):
        for y in range(-h, h):
            setpos(x * k, y * k)
            dot()

left(90)
pendown()

for i in range(2):
    forward(6 * k)
    right(90)
    forward(7 * k)
    right(90)
penup()
backward(2 * k)
right(90)
backward(3 * k)
left(90)
pendown()
for i in range(2):
    forward(5 * k)
    right(90)
    forward(6 * k)
    right(90)

penup()

grid(20, 20)
done()
