file = open("1.txt")
n = int(file.readline())

changes = [0] * (24 * 60 + 2)
visitors = [0] * (24 * 60 + 2)
for line in file:
    start, end = map(int, line.split())
    changes[start] += 1
    changes[end + 1] -= 1

cnt = 0
for t in range(24 * 60):
    cnt += changes[t]
    visitors[t] = cnt

print(max(visitors))
