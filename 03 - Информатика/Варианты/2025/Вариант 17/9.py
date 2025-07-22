file = open("9.txt")

max_diff = (0, 0)
for line in file:
    date, *data = line.split()
    data = list(map(float, data))
    month, day, year = map(int, date.split('/'))
    if month == 5:
        diff = round(data[8] - data[7], 2)
        if diff >= max_diff[0]:
            max_diff = (diff, day)
print(max_diff)
