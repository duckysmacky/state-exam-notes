from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20
penup()

pendown()
for _ in range(100):
    forward(10 * k)
    right(180)
    forward(10 * k)
    right(198)

done()
