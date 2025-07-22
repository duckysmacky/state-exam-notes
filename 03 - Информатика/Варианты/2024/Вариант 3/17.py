file = open("Задание 17/17.txt")
nums = list(map(int, file.readlines()))

nums_4 = [n for n in nums if n % 4 == 0]
avg = sum(nums_4) / len(nums_4)

def check(a, b):
    return a % min(nums) == 0 or b % min(nums) == 0

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]
    if check(*pair) and sum(pair) < avg:
        pairs.append(pair)
print(len(pairs), sum(max(pairs, key=sum)))