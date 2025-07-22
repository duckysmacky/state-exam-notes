def find_divs(x):
    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if div * div == x:
            divs.append(div)
        elif x % div == 0:
            divs.append(div)
            divs.append(x // div)
    return divs

N = 800_000
cnt = 0
for num in range(N, N + 1000):
    divs = find_divs(num)
    filtered = list(filter(lambda x: x != 3 and x % 10 == 3, divs))
    if len(filtered) > 0:
        print(num, max(filtered))
        cnt += 1
    if cnt == 2:
        break