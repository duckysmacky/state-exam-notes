from turtle import *

tracer(0)
screensize(10000, 10000)
k = 20
left(90)

penup()
forward(100 * k)
right(90)
forward(100 * k)
right(30)
pendown()
for _ in range(10):
    forward(30 / 10 * k)
    right(90)
    forward(40 / 10 * k)
    right(90)

penup()
for x in range(50, 200):
    for y in range(40, 120):
        setpos(x * k, y * k)
        dot()

done()
