file = open('3.txt')
n, n_rows, n_seats = map(int, file.readline().split())

seats = [[0, n_rows + 1] for _ in range(n_seats + 1)]
for line in file:
    row, seat = map(int, line.split())
    seats[seat].append(row)

distances = []
for i in range(1, len(seats)):
    seats[i].sort()
    for j in range(len(seats[i]) - 1):
        closest, furthest = seats[i][j], seats[i][j + 1]
        distances.append((furthest - closest - 2, -(furthest - 1), -i))

print(max(distances))