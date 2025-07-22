file = open("17.txt")
nums = list(map(int, file.readlines()))
triples = []

def check(tri):
    return sum(str(x)[-1] == '0' for x in tri) == 1

for i in range(len(nums) - 2):
    triple = nums[i:i + 3]
    if check(triple) and sum(triple) < max(nums):
        triples.append(triple)

print(len(triples), sum(max(triples, key=sum)))
