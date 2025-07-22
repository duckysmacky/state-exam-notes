file = open("17.txt")
nums = list(map(int, file.readlines()))
triples = []

def num_sum(num):
    return sum(map(int, str(num)))

sum_all = sum(num_sum(x) for x in nums if x % 12 == 0)

def check(nums):
    vals = 0
    for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        vals += nums[a] % (num_sum(nums[b]) + num_sum(nums[c])) == 0
    return vals == 1

for i in range(len(nums) - 2):
    triple = nums[i:i + 3]
    if check(triple) and sum(triple) < sum_all:
        triples.append(triple)

print(len(triples), sum(max(triples, key=sum)))
