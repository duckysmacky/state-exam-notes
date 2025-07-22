file = open("4.txt")

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    avg = sum(nums) / len(nums)
    if avg > 30:
        cnt += 1
print(cnt)
