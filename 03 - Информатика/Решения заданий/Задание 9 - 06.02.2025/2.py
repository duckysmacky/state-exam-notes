file = open("2.txt")
time = list(file.readline().split())

a, b = 0, 0
for line in file:
    date, *data = line.split()
    data = list(map(float, data))
    for x in data:
        if x > 4: a += 1
        if x < 2.5: b += 1
print(abs(a - b))
