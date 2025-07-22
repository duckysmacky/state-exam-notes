file = open("9.txt")

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    if nums[-1] > sum(nums[:3]) and len(set(nums)) == len(nums):
        cnt += 1
print(cnt)
