file = open("Задание 17/17.txt")
nums = list(map(int, file.readlines()))

min_num = min(x for x in nums if str(x)[-2:] == "11")

def check(pair: list) -> bool:
    return any(len(str(x)) != 3 for x in pair) and sum(pair) % min_num == 0

pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]
    if check(pair):
        pairs.append(pair)
print(len(pairs), sum(max(pairs, key=sum)))