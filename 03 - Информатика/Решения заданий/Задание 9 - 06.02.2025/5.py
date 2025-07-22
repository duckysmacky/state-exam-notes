file = open("5.txt")

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    if nums[0] ** 2 + nums[-1] ** 2 > sum(map(lambda x: x ** 2, nums[1:4])):
        cnt += 1
print(cnt)
