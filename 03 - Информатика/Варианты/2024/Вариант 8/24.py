file = open("files/24.txt")
print(min(map(lambda x: len(x), file.readline().split())))
