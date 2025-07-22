N = 400_000

def find_divs(x):
    divs = []
    for div in range(2, x):
        if x % div == 0:
            divs.append(div)
    return divs

cnt = 0
for num in range(N, N + 1000):
    divs = find_divs(num)
    if len(divs) == 0: continue
    if min(divs) * max(divs) % len(divs) == 0:
        print(num, max(divs))
        cnt += 1
    if cnt == 6:
        break