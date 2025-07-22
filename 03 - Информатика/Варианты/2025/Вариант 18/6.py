from turtle import *

k = 20
tracer(0); screensize(2000, 2000); left(90)

pendown()
for _ in range(2):
    forward(k * 17)
    left(90)
    forward(k * 10)
    left(90)
penup()
backward(k * 4)
right(90)
backward(k * 3)
left(90)
pendown()
for _ in range(2):
    forward(k * 40)
    right(90)
    forward(k * 10)
    right(90)
penup()

for x in range(-20, 20):
    for y in range(-10, 40):
        setpos(k * x, k * y)
        dot()

done()
