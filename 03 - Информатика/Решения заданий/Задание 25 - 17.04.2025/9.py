import re

pattern = r"18\d628\d*"
div = 666
for num in range(999999666, 1, -666):
    if re.match(pattern, str(num)) and num % div == 0:
        print(num, num // div)
        break