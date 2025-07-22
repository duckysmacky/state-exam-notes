file = open("1.txt")
n = int(file.readline())
time = [list(map(int, line.split())) for line in file]
time.sort(key=lambda x: x[1])

last_end = 0
valid = []
for start, end in time:
    if start >= last_end:
        last_end = end
        valid.append((start, end))
    if start >= 1344:
        print((start, end))
print(len(valid))
print(valid) # 1344
# 36 1438
