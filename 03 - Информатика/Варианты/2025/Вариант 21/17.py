file = open('17.txt')
nums = list(map(int, file.readlines()))

def check(triple):
    x = triple[1]
    return x > 0 and len(str(x)) == 3 and x % 10 == 5

triples = []
for i in range(len(nums) - 2):
    triple = nums[i:i + 3]
    if check(triple):
        triples.append(triple)
print(len(triples), sum(max(triples, key=sum)))