file = open("3-test.txt")
total, n_first, n_second = map(int, file.readline().split())
points = sorted(list(map(int, file.readlines())), reverse=True)

first = points[:n_first]
second = points[n_first:n_first + n_second]
avg = lambda l: int(sum(l) / len(l))
print(avg(second), first[-1])
