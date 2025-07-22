from math import ceil

file = open("2.txt")
n = int(file.readline())
prices = sorted(list(map(int, file.readlines())), reverse=True)

final = 0
over = []
for price in prices:
    if price > 120:
        over.append(price)
    else:
        final += price
over.sort()
discount, no_discount = over[:len(over) // 2], over[len(over) // 2:]
final += sum(no_discount) + sum(map(lambda x: x - x * 0.25, discount))
print(ceil(final), max(discount))
