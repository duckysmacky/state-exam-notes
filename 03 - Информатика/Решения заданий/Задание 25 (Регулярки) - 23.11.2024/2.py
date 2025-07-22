import re

for num in range(0, 10 ** 9, 127):
    if re.match("215\d*414\d", str(num)) and num % 127 == 0:
        print(num, num // 127)