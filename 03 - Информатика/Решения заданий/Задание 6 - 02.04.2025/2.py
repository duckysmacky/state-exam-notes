from turtle import *

tracer(0)
screensize(2000, 2000)
pendown()
k = 20

for _ in range(2):
    forward(17 * k)
    left(90)
    forward(34 * k)
    left(90)
penup()
forward(10 * k)
right(90)
forward(15 * k)
right(90)
pendown()
for _ in range(2):
    forward(40 * k)
    right(90)
    forward(24 * k)
    right(90)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot()

done()
