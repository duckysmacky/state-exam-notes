val = 49 ** 1010 + 7 ** 1000 - 7 ** 250
num = ""
while val > 0:
    num += str(val % 7)
    val //= 7
print(num.count('6'))
