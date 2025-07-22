from math import prod

file = open("9.csv")

def is_prog(nums):
    diffs = [abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)]
    return len(set(diffs)) == 1

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split(','))))
    if nums[-1] ** 2 > prod(nums[:-1]) or is_prog(nums):
        cnt += 1
print(cnt)
