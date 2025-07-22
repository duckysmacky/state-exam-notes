from turtle import *

k = 20
tracer(0)
screensize(2000, 2000)

pendown()
right(90)
for i in range(15):
    forward(5 * k)
    left(75)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * k, y * k)
        dot()

done()
