from turtle import *

k = 50
tracer(0)

pendown()
left(90)
right(45)
forward(4 * k)
for _ in range(10):
    right(45)
    forward(7 * k)
    right(135)
    forward(4 * k)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
