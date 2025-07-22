file = open("9.csv")
time = file.readline().split(',')[1:]

print(time[:13])

temps = []
for line in file:
    date, *temp = line.split(',')
    if date[0] != '6': continue
    temps += list(map(float, temp[:13]))

avg = lambda x: sum(x) / len(x)
print(max(temps), avg(temps))
print(abs(max(temps) - avg(temps)))
