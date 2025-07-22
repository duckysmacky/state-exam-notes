from turtle import *

k = 100
tracer(0)

left(90)
begin_fill()
pendown()

right(90)
for _ in range(3):
    right(45)
    forward(10 * k)
    right(45)
right(315)
forward(10 * k)
for _ in range(2):
    right(90)
    forward(10 * k)

penup()
end_fill()

canvas = getcanvas()
cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        overlaps = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if overlaps == (5,): cnt += 1
print(cnt)

done()
