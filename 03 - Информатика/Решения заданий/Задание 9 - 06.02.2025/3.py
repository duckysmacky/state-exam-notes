file = open("3.txt")

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    if sum(nums[:2]) > nums[2]:
        cnt += 1
print(cnt)
