file = open('26.txt')
n = int(file.readline())

data = []
for line in file:
    start, length = map(int, line.split())
    end = start + length
    data.append((end, start))
data.sort()
schedule = [(0, 0)]
starts = []
for end, start in data:
    if start >= schedule[-1][1]:
        schedule.append((start, end))
    # this value is the end of the second-last event to then check the most late start
    if start >= 1300:
        starts.append(start)
schedule.pop(0)
print(schedule[-5:])
print(len(schedule))
print(max(starts) - 1300)
# 26 20
