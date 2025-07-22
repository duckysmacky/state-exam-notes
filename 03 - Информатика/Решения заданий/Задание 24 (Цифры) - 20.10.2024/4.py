file = open("4.txt")
text = file.readline()
nums = []
j = 0
for i in range(1, len(text)):
    buff = text[j:i]
    if sum(int(n) ** len(buff) for n in buff) == int(buff) and int(buff) <= 10 ** 5:
        nums.append(int(buff))
    else:
        j = i
print(max(nums))