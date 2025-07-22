def find_divs(x: int) -> list:
    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            divs.append(div)
            divs.append(x // div)
    return divs

cnt = 0
start = 1_000_000
for num in range(start + 1, start + 1000):
    M = 0
    divs = find_divs(num)
    if len(divs) > 0:
        M = min(divs) + max(divs)
    if str(M)[-1] == '6':
        print(num, M)
        cnt += 1
    if cnt == 5:
        break
