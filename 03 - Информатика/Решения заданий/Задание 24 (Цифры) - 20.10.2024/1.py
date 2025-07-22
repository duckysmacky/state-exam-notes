file = open("1.txt")
text = file.readline()
nums = []
j = 0
for i in range(len(text)):
    buff = text[j:i]
    if buff.isdigit():
        if len(buff) == 6 and buff[0] != '0':
            nums.append(int(buff))
    else:
        j = i
print(min(nums))