file = open("17var02.txt")
nums = list(map(int, file.readlines()))

elem = min(nums)

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]
    if any(x % 30 == elem for x in pair):
        pairs.append(pair)
print(len(pairs), sum(min(pairs, key=sum))
