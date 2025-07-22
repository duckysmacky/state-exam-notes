file = open("17.txt")
nums = list(map(int, file.readlines()))

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]
    if any(x % 10 == 7 for x in pair) and sum(pair) % 12 == 0:
        pairs.append(pair)
print(len(pairs), sum(max(pairs, key=sum)))
