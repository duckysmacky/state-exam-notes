file = open("data.txt")
cnt = 0
for line in file:
    nums = list(map(int, line.split()))
    if sum(map(lambda x: x % 3, nums)) == 5:
        cnt += 1
print(cnt)