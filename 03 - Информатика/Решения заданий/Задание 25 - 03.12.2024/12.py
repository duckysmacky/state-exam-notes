from itertools import combinations

def find_divs(x: int) -> list:
    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if x * x == div:
            divs.append(div)
        elif x % div == 0:
            divs.append(div)
            divs.append(x // div)
    return divs

cnt = 0
for k in range(1000):
    M = 7_000_000 + k
    divs = find_divs(M)
    if not any(a * b * c == M for a, b, c in combinations(divs, r=3)):
        print(k)
        cnt += 1
    if cnt == 5:
        break