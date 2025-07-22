from turtle import *

k = 20
tracer(0)

left(90)
pendown()

right(90)
for _ in range(4):
    right(90)
    forward(5 * k)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
