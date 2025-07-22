file = open("1.txt")
total, group = map(int, file.readline().split())
points = list(map(int, file.readlines()))
points.sort(reverse=True)

amazing, good = points[:group], points[group:group * 2]
avg = lambda l: sum(l) / len(l)

print(int(avg(good)), int(avg(amazing)))
