file = open("26.txt")
N = int(file.readline())
data = {}
for line in file:
    row, point = map(int, line.split())
    data[row] = data.get(row, []) + [point]
# len = max - min + 1
# black = max - min - 1
lines = {}
for row in data.keys():
    points = sorted(list(set(data[row])))
    if len(points) < 2: continue
    max_len = 0
    i, j = 0, 1
    while i < len(points) and j < len(points):
        seq = points[i:j + 1]
        black = points[j] - points[i + (len(seq) - 2)] - 1
        if black <= 10:
            length = points[j] - points[i] + 1
            max_len = max(max_len, length)
            j += 1
        else:
            i += 1
            j = i + 1
    lines[row] = max_len
max_line = max(lines, key=lines.get)
max_line_len = lines[max_line]
print(max_line_len, max(k for k in lines.keys() if lines[k] == max_line_len))
