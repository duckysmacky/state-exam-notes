file = open("files/26.txt")
max_length, total = map(int, file.readline().split())
data = sorted(int(x) for x in file.readlines())
max_valid = 0
not_valid = 10 ** 10
for i in range(1, total):
    for j in range(i, total):
        lengths = data[i:j + 1]
        if sum(lengths) <= max_length:
            max_valid = max(max_valid, len(lengths))
        else:
            not_valid = min(not_valid, len(data[j:]))
print(max_valid, not_valid)
