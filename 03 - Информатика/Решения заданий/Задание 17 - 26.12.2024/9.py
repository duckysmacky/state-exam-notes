file = open("9.txt")
nums = list(map(int, file.readlines()))

nmin = min(nums)

def check(pair: list) -> bool:
    return any([abs(x) % 123 == nmin for x in pair])


pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]

    if check(pair):
        pairs.append(pair)

print(len(pairs), sum(max(pairs, key=sum)))
