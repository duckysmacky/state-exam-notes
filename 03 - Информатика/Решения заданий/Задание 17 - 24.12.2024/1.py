file = open("1.txt")
nums = list(map(int, file.readlines()))
pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]
    if all(x % 8 == 0 for x in pair):
        pairs.append(pair)
diff = lambda l: abs(l[0] - l[1])
print(len(pairs), diff(min(pairs, key=diff)))
