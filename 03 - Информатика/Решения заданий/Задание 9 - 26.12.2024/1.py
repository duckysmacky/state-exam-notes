file = open("1.txt")

def check(nums: list) -> bool:
    return max(nums) + min(nums) == sum(nums[1:3])

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))

    if check(nums):
        cnt += 1
print(cnt)
