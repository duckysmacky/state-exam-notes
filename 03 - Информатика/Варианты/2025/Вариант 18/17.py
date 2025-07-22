file = open('17.txt')
nums = list(map(int, file.readlines()))

min_num = min([x for x in nums if len(str(x)) >= 2 and x % 100 == 25])

triples = []
for i in range(len(nums) - 2):
    triple = nums[i:i + 3]
    if sum(len(str(x)) == 2 for x in triple) == 1 and sum(triple) < min_num:
        triples.append(triple)
print(len(triples), sum(max(triples, key=sum)))
