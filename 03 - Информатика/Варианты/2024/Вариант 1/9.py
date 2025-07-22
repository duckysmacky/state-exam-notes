file = open("9.txt")
count = 0
for line in file:
    data = sorted(list(map(int, line.split())))
    unique = [x for x in data if data.count(x) == 1]
    repeating = [x for x in data if data.count(x) != 1]
    if len(repeating) == 2 and sum(data[2:]) > 2 * sum(data[:2]) and data[-1] % data[0] != 0:
        print(data)
        count += 1
print(count)