from turtle import *

k = 20
tracer(0); screensize(2000, 2000); left(90); pendown()

for _ in range(9):
    forward(12 * k)
    right(90)
    forward(6 * k)
    right(90)
penup()
forward(1 * k)
right(90)
forward(3 * k)
left(90)
pendown()
for _ in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot()

done()
