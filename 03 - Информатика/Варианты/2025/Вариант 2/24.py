file = open("24var02.txt")
text = file.readline().replace('-', '+')
print(text[:20])

max_val = ''
val = ''
for num in text.split('+'):
    if len(num) > 0:
        if num[0] != '0':
            val += num + '+'
        elif int(num) != 0:
            max_val = max(max_val, val, key=len)
            val = str(int(num)) + '+'
    else:
        val = ''
    max_val = max(max_val, val, key=len)
print(max_val)
print(len(max_val) - 1)
