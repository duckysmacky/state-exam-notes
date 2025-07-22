def find_divs(x: int) -> list:
    def check(d: int) -> bool: return d % 3 == 0 and d % 2 == 0

    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            if check(div): divs.append(div)
            if check(x // div): divs.append(x // div)
    return divs

test = range(85, 93 + 1)
actual = range(64_930, 65_050 + 1)
for num in actual:
    divs = find_divs(num)
    if len(set(divs)) == 3:
        print(num, ' '.join(map(str, sorted(divs))))
