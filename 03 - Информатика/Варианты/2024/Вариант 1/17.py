file = open("17.txt")
nums = list(map(int, file.readlines()))

def num_sum(num: int) -> int:
    return sum([int(x) for x in str(num)])

min_sum = min(num_sum(n) for n in nums)
max_min = max(n for n in nums if num_sum(n) == min_sum)
pairs = []

def check(a: int, b: int) -> bool:
    return a > max_min and b > max_min

for i in range(len(nums) - 1):
    pair = (nums[i], nums[i + 1])
    if check(*pair):
        pairs.append(pair)

print(len(pairs), max(sum(num_sum(x) for x in p) for p in pairs))