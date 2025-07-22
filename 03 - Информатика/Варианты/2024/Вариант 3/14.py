from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:13]:
    val = int(f"186{x}4", 13) + int(f"5{x}716", 13)
    if val % 11 == 0:
        print(val // 11)
        break