file = open("27/27-B.txt")
N = int(file.readline())
nums = list(map(int, file.readlines()))

found = []
i, j = 0, 0
while i < N:
    slc = nums[j:i + 1]
    if sum(slc) % 107 == 0:
        found.append(slc)

    j += 1
    if j > i:
        j = 0
        i += 1

print(len(min(sorted(found, reverse=True, key=sum)[:10], key=len)))