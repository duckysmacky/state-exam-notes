from turtle import *

tracer(0)
screensize(2000, 2000)
pendown()
left(90)
k = 20

for _ in range(3):
    forward(12 * k)
    right(120)
penup()
right(60)
forward(6 * k)
left(60)
pendown()
for _ in range(3):
    forward(15 * k)
    right(90)
    forward(24 * k)
    right(90)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot()

done()
