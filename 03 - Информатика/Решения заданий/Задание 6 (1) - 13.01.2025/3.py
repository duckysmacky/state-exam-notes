from turtle import *

k = 50
tracer(0)

pendown()
for _ in range(2):
    forward(13 * k)
    right(90)
    forward(5 * k)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
