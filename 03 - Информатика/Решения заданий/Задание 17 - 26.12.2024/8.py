file = open("8.txt")
nums = list(map(int, file.readlines()))

max_end6 = max([x for x in nums if str(x)[-1] == '6'])

def check(pair: list) -> bool:
    cnt_end6 = sum(str(x)[-1] == '6' for x in pair)
    return cnt_end6 == 1 and sum(x ** 2 for x in pair) < max_end6 ** 2


pairs = []
for i in range(len(nums) - 1):
    pair = nums[i:i + 2]

    if check(pair):
        pairs.append(pair)

sqsum = lambda l: sum(x ** 2 for x in l)

print(len(pairs), sqsum(max(pairs, key=sqsum)))
