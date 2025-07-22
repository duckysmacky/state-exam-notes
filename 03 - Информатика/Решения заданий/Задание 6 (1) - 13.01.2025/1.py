from turtle import *

tracer(0)
k = 20

left(90)
pendown()
for _ in range(9):
    right(80)
    forward(5 * k)
penup()

done()
