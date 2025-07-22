file = open("4.txt")
nums = list(map(int, file.readlines()))

def check(pair: list) -> bool:
    return any(x > 0 and (x ** 0.5) % 1 == 0 for x in pair)

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]
    if check(pair):
        pairs.append(pair)
print(len(pairs), sum(max(pairs, key=sum)))
