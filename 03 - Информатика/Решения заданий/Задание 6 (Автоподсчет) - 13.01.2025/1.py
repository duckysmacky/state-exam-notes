from turtle import *

k = 100
tracer(0)
screensize(3000, 3000)

pendown()
left(90)
#begin_fill()
for _ in range(21):
    forward(137 * k)
    right(120)
penup()
#end_fill()

canvas = getcanvas()
cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        overlaps = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if overlaps == (5,): cnt += 1
print(cnt)

done()
