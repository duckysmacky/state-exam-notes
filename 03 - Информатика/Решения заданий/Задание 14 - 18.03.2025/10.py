import string

alph = string.digits + string.ascii_uppercase
for x in alph[:17]:
    val = int(f"18{x}AE", 17) + int(f"733{x}C", 17)
    if val % 13 == 0:
        print(val // 13)
        break
