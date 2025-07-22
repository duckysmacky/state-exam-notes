file = open("12.txt")
nums = list(map(int, file.readlines()))

def numlen(x: int) -> int: return len(str(abs(x)))

def check(pair: list) -> bool:
    return numlen(sum(pair)) == 6 and any((x ** 0.5) % 1 == 0 for x in pair)

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]

    if check(pair):
        pairs.append(pair)

print(len(pairs), sum(max(pairs, key=sum)))
