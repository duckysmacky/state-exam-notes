file = open("2.txt")
text = file.readline()
nums = []
j = 0
for i in range(len(text)):
    buff = text[j:i]
    if buff.isdigit():
        if all(int(n) % 2 != 0 for n in buff):
            nums.append(int(buff))
    else:
        j = i
print(max(nums))