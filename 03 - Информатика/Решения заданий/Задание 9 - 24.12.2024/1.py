file = open("1.txt")

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    if len(set(nums)) == len(nums) and (nums[0] + nums[-1]) * 3 >= (sum(nums[1:-1])) * 2:
        cnt += 1
print(cnt)
