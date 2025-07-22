x = (256 ** 500) * (4 ** 100) - (64 ** 30) - 8
num = ""
while x > 0:
    num += str(x % 4)
    x //= 4

print(num[::-1].count('3'))
