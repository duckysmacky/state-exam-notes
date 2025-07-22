file = open("2.txt")
N = int(file.readline())
prices = list(map(int, file.readlines()))
wanted_price = sum(sorted(prices, reverse=True)[:len(prices) // 3]) * 0.5
real_price = sum(sorted(prices, reverse=False)[:len(prices) // 3]) * 0.5
print(int(sum(prices) - wanted_price), int(sum(prices) - real_price))