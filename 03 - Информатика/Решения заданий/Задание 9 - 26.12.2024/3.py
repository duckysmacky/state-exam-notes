file = open("3.txt")

avg = lambda l: sum(l) / len(l)

cnt = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    unique = [x for x in nums if nums.count(x) == 1]
    repeating = [x for x in nums if nums.count(x) != 1]

    if len(unique) == 4 and len(set(repeating)) == 1 and avg(repeating) > max(unique):
        cnt += 1
print(cnt)
