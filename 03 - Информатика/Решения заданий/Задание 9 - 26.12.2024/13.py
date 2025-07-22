file = open("13.txt")

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    unique = [x for x in nums if nums.count(x) == 1]
    repeating = [x for x in nums if nums.count(x) != 1]

    if len(repeating) == len(nums) // 2 and max(unique) ** 2 > sum(repeating) ** 2:
        cnt += 1
print(cnt)
