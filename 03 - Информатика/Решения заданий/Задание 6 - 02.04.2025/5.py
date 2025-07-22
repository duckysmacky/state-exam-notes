from turtle import *
import math

tracer(0)
screensize(2000, 2000)
pendown()
left(90)
k = 20

for _ in range(123):
    forward(111 * k)
    right(120)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot()

done()

cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        tg = math.tan(math.radians(30))
        if x > 0 and y > tg * x and y < -tg * x + 111:
            cnt += 1
print(cnt)
