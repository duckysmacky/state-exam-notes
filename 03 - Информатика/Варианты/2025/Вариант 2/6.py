from turtle import *

tracer(0)
k = 20

left(90)
pendown()
for _ in range(5):
    forward(30 * k)
    right(90)
    forward(40 * k)
    right(90)
penup()
forward(20 * k)
right(90)
forward(15 * k)
right(90)
pendown()
for _ in range(7):
    forward(10 * k)
    right(90)
penup()

r = range(0, 45)
for x in r:
    for y in r:
        setpos(x * k, y * k)
        dot()

done()
