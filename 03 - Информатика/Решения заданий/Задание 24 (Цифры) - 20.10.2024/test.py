file = open("test.txt")
text = file.readline()
nums = []
j = 0
for i in range(len(text)):
    buff = text[j:i]
    if buff.isdigit():
        if int(buff) % 2 != 0: nums.append(int(buff))
    else:
        j = i
print(max(nums))