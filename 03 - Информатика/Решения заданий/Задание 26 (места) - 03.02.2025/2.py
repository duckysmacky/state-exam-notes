file = open("2.txt")
n_occupied, m_rows, k_seats = map(int, file.readline().split())

seat_info = [[0, m_rows + 1] for _ in range(k_seats + 1)]
for line in file:
    row, seat = map(int, line.split())
    seat_info[seat].append(row)

best_seats = []
for rows in seat_info:
    rows = sorted(rows, reverse=True)
    for i in range(len(rows) - 1):
        upper, lower = rows[i], rows[i + 1]
        best_seats.append((upper - lower - 1 - 1, -(upper - 1)))
best_seats.sort(reverse=True)
print(best_seats[:5])
