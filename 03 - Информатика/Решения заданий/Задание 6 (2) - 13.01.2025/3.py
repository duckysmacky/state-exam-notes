from turtle import *

k = 30
tracer(0)

pendown()
left(90)
for _ in range(9):
    forward(5 * k)
    right(90)
    forward(4 * k)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
