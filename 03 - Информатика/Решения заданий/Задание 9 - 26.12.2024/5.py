file = open("5.txt")

def check(nums: list) -> bool:
    return all(x % 2 == 0 for x in nums) and nums[0] ** 2 <= sum(nums[1:])

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))

    if check(nums):
        cnt += 1
print(cnt)
