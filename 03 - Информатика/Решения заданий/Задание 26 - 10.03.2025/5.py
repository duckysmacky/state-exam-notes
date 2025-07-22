file = open("5.txt")
n = int(file.readline())
time = []
for line in file:
    start, end = map(int, line.split())
    time.append((end, start))
time.sort()
schedule = [(0, 0)]
for end, start in time:
    if start > schedule[-1][1]:
        schedule.append((start, end))
    if end < 78:
        print(start, end)
print(schedule)
print(len(schedule) - 1)
# 35 37
