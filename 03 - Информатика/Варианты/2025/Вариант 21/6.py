from turtle import *

tracer(0)
screensize(2000, 2000)
left(90)
pendown()
k = 20

right(198)
for _ in range(5):
    forward(10 * k)
    left(144)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot()

done()