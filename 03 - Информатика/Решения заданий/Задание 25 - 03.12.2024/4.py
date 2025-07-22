def find_divs(x: int) -> set:
    divs = set()
    for div in range(1, int(x ** 0.5) + 1):
        if x % div == 0:
            divs.add(div)
            divs.add(x // div)
    return divs

for num in range(200_123, 200_150 + 1):
    divs = find_divs(num)
    if len(divs) == 4:
        print(sorted(divs))