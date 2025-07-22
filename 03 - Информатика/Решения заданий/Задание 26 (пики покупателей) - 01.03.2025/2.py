file = open("2.txt")
n = int(file.readline())

changes = [0] * (24 * 60 * 60 + 2)
visitors = [0] * (24 * 60 * 60 + 2)
for line in file:
    start, end = map(int, line.split())
    changes[start] += 1
    changes[end] -= 1

cnt = 0
for t in range(len(changes)):
    cnt += changes[t]
    visitors[t] = cnt

period = visitors[8 * 60 * 60:14 * 60 * 60 + 1]
print(max(period))
print(period.count(max(period)))
