r = range(0, 8)

for a in r:
    for b in r:
        for c in range(0, 16):
            x1 = int(f"2{a}{b}50", 8)
            x2 = int(f"{c}C28", 16)
            if x1 == x2:
                print(x1, x2)
