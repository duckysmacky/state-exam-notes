def find_divs(x: int) -> set:
    divs = set()
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            divs.add(div)
            divs.add(x // div)
    return divs

for num in range(23_456, 78_954 + 1):
    divs = find_divs(num)
    if len(divs) == 3:
        print(num, max(divs))