file = open('2.txt')
n, n_rows, n_seats = map(int, file.readline().split())

seats = [1] * (n_seats + 1)
for line in file:
    row, seat = map(int, line.split())
    seats[seat] = max(seats[seat], row + 1)

avaliable = []
for i in range(1, len(seats) - 2):
    avaliable.append((max(seats[i:i + 3]), -(i + 2)))

print(min(avaliable))