def is_prime(x):
    if x < 2: return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True

cnt = 0
for num in range(2_358_827, 2_358_891 + 1):
    if is_prime(num):
        cnt += 1
        print(cnt, num)
