from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:12]:
    val = int(f"32D{x}", 16) + int(f"43{x}B", 12)
    if val % 15:
        print(str(val)[0])