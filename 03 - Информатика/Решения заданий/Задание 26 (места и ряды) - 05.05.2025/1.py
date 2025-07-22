file = open('test.txt')
n, n_rows, n_seats = map(int, file.readline().split())

seats = [n_rows] * (n_seats + 1)
for line in file:
    row, seat = map(int, line.split())
    seats[seat] = min(seats[seat], row - 1)

avaliable = []
for i in range(len(seats) - 1):
    avaliable.append((min(seats[i:i + 2]), -i))

print(max(avaliable))