cnt = 0
for num in range(600_000, 600_000 + 1000):
    for div in range(17, num, 10):
        if num % div == 0:
            print(num, div)
            cnt += 1
            break
    if cnt == 5:
        break