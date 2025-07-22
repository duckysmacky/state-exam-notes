file = open("3.txt")
nums = list(map(int, file.readlines()))

def check(triple: list) -> bool:
    return any(x < 0 for x in triple)

triples = []
for i in range(len(nums) - 2):
    triple = nums[i:i + 3]
    if check(triple):
        triples.append(triple)

print(len(triples), sum(min(triples, key=sum)))
