file = open('9.csv')

cnt = 0
for line in file:
    nums = list(map(int, line.split(',')))
    repeating = [x for x in nums if nums.count(x) > 1]
    unique = [x for x in nums if nums.count(x) == 1]
    if len(unique) == 2 and all([repeating.count(x) == 3 for x in repeating]) and max(nums) not in repeating:
        cnt += 1
print(cnt)
