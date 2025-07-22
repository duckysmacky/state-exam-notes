from turtle import *

k = 30
tracer(0)

pendown()
for _ in range(16):
    forward(5 * k)
    left(70)
    backward(2 * k)
    right(10)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
