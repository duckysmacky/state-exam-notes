def is_prime(x):
    if x < 2: return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True

def find_divs(x):
    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if div * div == x:
            divs.append(div)
        elif x % div == 0:
            divs.append(div)
            divs.append(x // div)
    divs.sort(reverse=True)
    return divs[:2]

cnt = 0
N = 200_000
for num in range(N, N + 1000):
    divs = find_divs(num)
    if len(divs) == 2 and all(map(is_prime, divs)):
        cnt += 1
        print(divs)
    if cnt == 2:
        break