file = open("2.txt")
nums = list(map(int, file.readlines()))

def check(pair: list) -> bool:
    return any(x > 500 for x in pair)

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]
    if check(pair):
        pairs.append(pair)
sq_sum = lambda p: sum(x ** 2 for x in p)
print(len(pairs), sq_sum(max(pairs, key=sq_sum)))
