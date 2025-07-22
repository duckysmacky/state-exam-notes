file = open("3.txt")
n = int(file.readline())
data = []
for line in file:
    start, end = map(int, line.split())
    data.append((end, start))
data.sort()
schedule = [(0, 0)]
for end, start in data:
    if start >= schedule[-1][1]:
        schedule.append((start, end))
    if start >= 1344:
        print(start, end)
print(schedule)
print(len(schedule) - 1)
# 37 1438
