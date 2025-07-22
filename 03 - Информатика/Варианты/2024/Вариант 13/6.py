from turtle import *

k = 20
screensize(2000, 2000)
tracer(0)

def mv(a: int, b: int) -> None:
    x, y = pos()
    setpos(x + (a * k), y + (b * k))

pendown()
for _ in range(5):
    mv(1, 6)
    mv(7, -4)
    mv(-6, -5)
    mv(-2, 3)

penup()
for y in range(-20, 20):
    for x in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()
