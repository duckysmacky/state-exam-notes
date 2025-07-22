def conv(x: int, p: int) -> str:
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

def is_prime(x: int) -> bool:
    if x < 2: return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True

ans = 0
for p in range(2, 11):
    num = conv(437, p)
    nsum = sum(map(int, num))
    if is_prime(nsum):
        ans += p
print(ans)
