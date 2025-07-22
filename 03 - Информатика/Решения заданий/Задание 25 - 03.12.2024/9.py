def find_divs(x: int) -> list:
    divs = []
    for div in range(1, int(x ** 0.5) + 1):
        if x * x == div:
            divs.append(div)
        elif x % div == 0:
            divs.append(div)
            divs.append(x // div)
    return divs


def is_prime(x: int) -> bool:
    if x < 2: return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True

N = 600_000
for num in range(N, N + 1000):
    divs = find_divs(num)
    prime_divs = [d for d in divs if is_prime(d)]
    if not is_prime(len(divs)) and len(prime_divs) % 2 == 0:
        print(num, len(prime_divs))
        break