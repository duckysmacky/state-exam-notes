from turtle import *

k = 50
tracer(0)

pendown()
left(90)
for _ in range(7):
    forward(10 * k)
    right(120)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
