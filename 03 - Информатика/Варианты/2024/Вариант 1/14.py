x = 7 * 5 ** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10
num = ''
while x > 0:
    num += str(x % 5)
    x //= 5
num = num[::-1]
print(num.count('4'))