file = open("1.txt")
time = list(file.readline().split())

cnt = 0
for line in file:
    date, *temp = line.split()
    temp = list(map(float, temp))
    avg = sum(temp) / len(temp)
    if temp[12] > avg:
        cnt += 1
print(cnt)
