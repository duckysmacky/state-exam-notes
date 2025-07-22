import re

for num in range(0, 10 ** 7, 403):
    if re.match("12\d*\d1\d*5", str(num)):
        print(num, num // 403)