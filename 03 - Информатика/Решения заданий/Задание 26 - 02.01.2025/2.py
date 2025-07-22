file = open("2.txt")
total, k_bad = map(int, file.readline().split())

burners = {}
for line in file:
    row, val = map(int, line.split())
    burners[row] = sorted(burners.get(row, []) + [val])

rows = {}
for r in burners.keys():
    row = burners[r]
    for i in range(len(row) - 1):
        max_dist = 0
        dist = row[i + 1] - row[i] - 1
        if dist == k_bad and dist > max_dist:
            max_dist = dist
            rows[r] = row[i] + 1
max_row = max(rows.keys())
print(max_row, rows[max_row])
