file = open("Задание 9/9.txt")

cnt = 0
for line in file:
    nums = list(map(int, line.split()))
    repeating = [x for x in nums if nums.count(x) > 1]
    unique = [x for x in nums if nums.count(x) == 1]
    if len(set(unique)) == 4 and sum(unique) < 100:
        cnt += 1
print(cnt)