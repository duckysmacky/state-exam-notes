file = open("3.txt")
N = int(file.readline())
data = sorted(list(map(int, file.readlines())), reverse=True)
wanted_discount = sum(data[:len(data) // 3])
real_discount = 0
for i in range(N):
    if (i + 1) % 3 == 0:
        real_discount += data[i]
print(sum(data) - wanted_discount, sum(data) - real_discount)