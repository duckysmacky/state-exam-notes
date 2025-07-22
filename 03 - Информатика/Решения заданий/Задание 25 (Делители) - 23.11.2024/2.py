for num in range(14_620, 15_000 + 1):
    divs = []
    for div in range(2, num):
        if num % div == 0:
            divs.append(div)
    if len(divs) == 3:
        print(num, min(divs))