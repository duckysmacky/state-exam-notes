file = open('26.txt')
n = int(file.readline())
nums = list(map(int, file.readlines()))
nums.sort()

max_step = 100

pairs = []
for i in range(len(nums)):
    for step in range(max_step + 2):
        j = i + step
        if j >= len(nums): break
        pair = (nums[i], nums[j])
        if len(set(pair)) == 2 and sum(pair) % 10 == 0:
            pairs.append(pair)

avg = lambda x: sum(x) / len(x)
print(nums)
print(pairs)
print(len(pairs), avg(min(pairs, key=avg)))