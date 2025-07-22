from turtle import *

k = 30
tracer(0)

pendown()
for _ in range(5):
    forward(10 * k)
    right(144)
    forward(10 * k)
    left(72)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
