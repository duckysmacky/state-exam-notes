file = open("11.txt")
nums = list(map(int, file.readlines()))

def numlen(x: int) -> int: return len(str(abs(x)))

min_num = min([x for x in nums if abs(x) % 1000 == 600])

def check(triple: list) -> bool:
    return sum(numlen(x) == 5 for x in triple) <= 2 and sum(triple) >= min_num

triples = []
for i in range(len(nums) - 2):
    triple = nums[i:i + 3]

    if check(triple):
        triples.append(triple)

print(len(triples), sum(min(triples, key=sum)))
