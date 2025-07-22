from turtle import *

k = 20
tracer(0)
screensize(2000, 2000)

pendown()
for _ in range(2):
    forward(16 * k)
    right(90)
    forward(9 * k)
    right(90)

penup()
forward(5 * k)
right(90)
forward(11 * k)
right(90)

pendown()
for _ in range(2):
    forward(20 * k)
    right(90)
    forward(8 * k)
    right(90)

penup()
for x in range(-30, 20):
    for y in range(-30, 20):
        setpos(x * k, y * k)
        dot()

print(9 * 21)
print(16 * 9)

done()