from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in range(18):
    val = int(f"AB5{alph[x]}3", 18) + int(f"EF{alph[x]}13", 18)
    if val % 17 == 0:
        print(val // 17)
        break