file = open("7.txt")
nums = list(map(int, file.readlines()))

max14 = max([x for x in nums if x % 14 == 0])

triples = []
for i in range(len(nums) - 2):
    triple = nums[i:i + 3]

    if sum(len(str(abs(x))) == 4 for x in triple) == 1 and sum(triple) <= max14:
        triples.append(triple)

print(len(triples), sum(max(triples, key=sum)))
