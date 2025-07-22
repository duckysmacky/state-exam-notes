from turtle import *

k = 30
tracer(0)

pendown()
left(90)
for _ in range(12):
    forward(5 * k)
    right(120)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
