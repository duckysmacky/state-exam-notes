file = open("17.txt")
nums = list(map(int, file.readlines()))
triples = []

nums17 = [x for x in nums if x % 17 != 0]
avg = sum(nums17) / len(nums17)

def conv(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

def is_polydrom(num):
    return num == num[::-1]

def check(triple):
    sum5 = conv(sum(triple), 5)
    return is_polydrom(sum5) and max(triple) < avg

for i in range(len(nums) - 2):
    triple = nums[i:i + 3]
    if check(triple):
        triples.append(triple)
print(len(triples), sum(max(triples, key=sum)))
