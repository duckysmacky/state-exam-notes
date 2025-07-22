from turtle import *

k = 50
tracer(0)

pendown()
left(90)
for _ in range(15):
    right(90)
    forward(k)
    left(45)
    backward(k)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * k, y * k)
        dot()

done()
