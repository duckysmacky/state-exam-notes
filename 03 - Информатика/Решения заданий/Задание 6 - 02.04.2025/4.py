from turtle import *

tracer(0)
screensize(2000, 2000)
pendown()
left(90)
k = 20

for _ in range(6):
    forward(3 * k)
    right(90)
penup()
forward(1 * k)
right(270)
forward(1 * k)
right(90)
pendown()
for _ in range(6):
    forward(4 * k)
    right(90)
    forward(5 * k)
    right(90)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot()

done()
