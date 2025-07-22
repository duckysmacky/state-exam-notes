def is_prime(x: int) -> bool:
    for d in range(2, int(num ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


cnt = 0
for num in range(610_001, 610_000 + 1000):
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            if is_prime(num // d):
                print(num, num // d)
                cnt += 1
                break
    if cnt == 6:
        break