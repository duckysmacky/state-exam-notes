from math import prod

file = open("6.txt")

avg = lambda l: sum(l) / len(l)

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    unique = [x for x in nums if nums.count(x) == 1]
    repeating = [x for x in nums if nums.count(x) != 1]

    if len(repeating) == 2 and oct(sum(map(int, str(prod(repeating)))) ** 2)[-1] == '0':
        cnt += 1
print(cnt)
