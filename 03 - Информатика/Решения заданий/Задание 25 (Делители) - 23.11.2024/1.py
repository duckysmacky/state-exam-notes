for num in range(200_123, 200_150 + 1):
    divs = []
    for div in range(1, num + 1):
        if num % div == 0:
            divs.append(div)
    if len(divs) == 4:
        print(divs)