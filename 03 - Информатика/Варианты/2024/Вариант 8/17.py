file = open("files/17.txt")
nums = list(map(int, filter(lambda x: '4' in str(x), file.readlines())))
print(len(nums), max(nums))
