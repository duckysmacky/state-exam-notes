def is_prime(x: int) -> bool:
    if x < 2: return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True

r = range(250_000_000, 1_000_000_000 + 1)
for m in range(2, 14):
    if not is_prime(m): continue
    for n in range(2, 10 + 1, 2):
        N = (2 ** m) * (5 ** n)
        if N in r:
            print(N, m ** 2 + n ** 2)