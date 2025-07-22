file = open("Задание 9/9.csv")
cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split(';'))))
    if nums[0] + nums[-1] < 2 * (nums[1] + nums[2]):
        cnt += 1
print(cnt)