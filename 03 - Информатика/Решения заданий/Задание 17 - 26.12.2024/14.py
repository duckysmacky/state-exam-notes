file = open("14.txt")
nums = list(map(int, file.readlines()))

def numlen(x: int) -> int: return len(str(abs(x)))

def check(pair: list) -> bool:
    return all(numlen(x) == int(str(abs(x))[0]) for x in pair)

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]

    if check(pair):
        pairs.append(pair)

print(len(pairs), sum(min(pairs, key=sum)))
