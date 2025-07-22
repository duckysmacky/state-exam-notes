from turtle import *

tracer(0)
screensize(2000, 2000)
pendown()
left(90)
k = 20

for _ in range(2):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)
penup()
forward(5 * k)
right(90)
forward(7 * k)
left(90)
pendown()
for _ in range(2):
    forward(10 * k)
    right(90)
    forward(7 * k)
    right(90)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot()

done()
