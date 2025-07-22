def is_prime(x: int) -> bool:
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True


cnt = 0
for num in range(700_000, 700_000 + 1000):
    f = 0
    for div in range(2, num):
        if num % div == 0 and is_prime(div):
            f = num // div - div
            break
    if f != 0 and f % 9 == 0:
        print(num, f)
        cnt += 1
    if cnt == 5:
        break