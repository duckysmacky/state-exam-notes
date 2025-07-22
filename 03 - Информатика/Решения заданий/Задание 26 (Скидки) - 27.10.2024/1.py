from math import ceil

file = open("1.txt")
N = int(file.readline())
prices = sorted(list(map(int, file.readlines())))
prices_120 = [x for x in prices if x > 120]
prices_sale = prices_120[:len(prices_120) // 2]
sum_sale = sum(prices_sale) * 0.25
print(ceil(sum(prices) - sum_sale), max(prices_sale))