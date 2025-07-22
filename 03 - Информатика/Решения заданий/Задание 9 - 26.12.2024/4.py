from itertools import permutations
from math import prod

file = open("4.txt")

def pairs(nums: list) -> bool:
    for comb in permutations(nums, r=4):
        left, right = comb[:2], comb[2:]
        if prod(left) == prod(right):
            return True
    return False

def check(nums: list) -> bool:
    return pairs(nums) and max(nums) ** 2 <= min(nums) * max(nums)

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))

    if check(nums):
        cnt += 1
print(cnt)
