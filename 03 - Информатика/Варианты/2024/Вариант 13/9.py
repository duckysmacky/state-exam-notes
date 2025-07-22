file = open("Задание 9/9.csv")

max_val = -10 ** 9
min_val = 10 ** 10
for line in file:
    date, *data = line.replace(',', '.').split(";")
    data = list(map(float, data))
    max_val = max(max_val, max(data))
    min_val = min(min_val, min(data))
print(max_val - min_val)
