file = open("1.txt")
n_occupied, m_rows, k_seats = map(int, file.readline().split())

seat_info = [m_rows] * (k_seats + 1)
for line in file:
    row, seat = map(int, line.split())
    seat_info[seat] = min(seat_info[seat], row - 1)

best_seats = []
for seat in range(1, len(seat_info) - 1):
    left_row, right_row = seat_info[seat], seat_info[seat + 1]
    best_seats.append([min(left_row, right_row), seat, seat + 1])
best_seats.sort(reverse=True)
print(best_seats[0]) # 5 7
