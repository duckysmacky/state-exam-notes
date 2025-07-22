from string import digits, ascii_uppercase
file = open("3.txt")
text = file.readline()
nums = []
buff = text[0]
digits_17 = (digits + ascii_uppercase)[:17]
for i in range(len(text) - 1):
    if text[i] in digits_17 and text[i + 1] in digits_17:
        buff += text[i + 1]
        nums.append(buff)
    else:
        buff = text[i + 1]
print(len(max(nums, key=len)))