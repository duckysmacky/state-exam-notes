from turtle import *

k = 20
tracer(0)

left(90)

for _ in range(3):
    pendown()
    for _ in range(2):
        forward(10 * k)
        right(90)
        forward(10 * k)
        right(90)
    penup()
    forward(10 * k)
    right(90)
    forward(5 * k)
    right(90)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
