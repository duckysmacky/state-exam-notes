file = open("1.txt")
n = int(file.readline())
slices = list(map(int, file.readlines()))
slices.sort(reverse=True)
print(slices)
cake = [slices.pop(0)]
for slice in slices:
    if (cake[-1] - slice) >= 7:
        cake.append(slice)
print(cake)
print(len(cake), cake[-1])
