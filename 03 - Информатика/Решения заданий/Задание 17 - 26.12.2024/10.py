file = open("10.txt")
nums = list(map(int, file.readlines()))

def numlen(x: int) -> int: return len(str(abs(x)))

min_num = min([x for x in nums if numlen(x) == 2])

def check(pair: list) -> bool:
    return all([numlen(x) == 2 for x in pair]) and sum(pair) % min_num == 0

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]

    if check(pair):
        pairs.append(pair)

print(len(pairs), sum(max(pairs, key=sum)))
