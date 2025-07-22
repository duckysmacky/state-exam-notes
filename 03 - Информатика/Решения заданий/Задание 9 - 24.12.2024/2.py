file = open("2.txt")

cnt = 0
for line in file:
    nums = list(map(int, line.split()))
    unique = [x for x in nums if nums.count(x) == 1]
    repeating = [x for x in nums if nums.count(x) > 1]

    if len(set(nums)) == 4 and sum(repeating) < sum(unique):
        cnt += 1

print(cnt)
