file = open("3.txt")

cnt = 0
for line in file:
    nums = list(map(int, line.split()))
    unique = [x for x in nums if nums.count(x) == 1]
    repeating = [x for x in nums if nums.count(x) > 1]

    if len(repeating) > 0 and sum(unique) % 2 != 0:
        cnt += 1

print(cnt)
