def find_divs(x: int) -> list:
    divs = []
    for div in range(17, x, 10):
        if x % div == 0:
            divs.append(div)
    return divs

cnt = 0
for num in range(600_000, 600_000 + 1000):
    divs = find_divs(num)
    if len(divs) > 0:
        print(num, min(divs))
        cnt += 1
    if cnt == 5:
        break