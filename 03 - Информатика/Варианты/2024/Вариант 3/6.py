from turtle import *

k = 20
screensize(2000, 2000)
tracer(0)

pendown()
for _ in range(9):
    forward(8 * k)
    left(120)

penup()
for y in range(-20, 20):
    for x in range(-20, 20):
        setpos(y * k, x * k)
        dot()

done()