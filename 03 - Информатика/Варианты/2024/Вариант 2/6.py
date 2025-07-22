from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20

pendown()
right(90)
for i in range(15):
    forward(2 * k)
    right(180)
    for j in range(4):
        right(270)
        forward(4 * k)

penup()
for y in range(-20, 20):
    for x in range(-20, 20):
        setpos(y * k, x * k)
        dot()

done()