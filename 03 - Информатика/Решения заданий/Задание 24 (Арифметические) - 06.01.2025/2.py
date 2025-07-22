file = open("2.txt")
text = file.readline().replace('-', '*')
text = "1561*00000*8156***12*0*617777*126**06126*1263"

max_val = ''
val = ''
for num in text.split('*'):
    if len(num) > 0:
        if num[0] != '0' or num == '0':
            val += num + '*'
        elif num[0] == '0':
            val += "0*"
            max_val = max(max_val, val, key=len)
            val = str(int(num)) + '*'
    else:
        val = ''
    max_val = max(max_val, val, key=len)

print(max_val)
print(len(max_val) - 1)