from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:20]:
    val = int(f"13{x}CF", 20) + int(f"47GH{x}", 20)
    if val % 19 == 0:
        print(val // 19)
        break