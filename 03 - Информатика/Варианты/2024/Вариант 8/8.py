ans = 0
nums_chet = [0, 2, 4, 6, 8]
nums_nechet = [1, 3, 5, 7, 9]


def count(x: str, nums: list) -> int:
    total = 0
    for num in nums:
        total += x.count(str(num))
    return total


for x in range(100000, 1000000):
    x = str(x)
    if x[-2:] == "34" and len(set(x)) == len(x) \
            and (count(x, nums_chet) == 3 or count(x, nums_nechet) == 2):
        ans += 1
print(ans)
