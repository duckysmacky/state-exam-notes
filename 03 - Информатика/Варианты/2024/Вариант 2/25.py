nums = []
for x in range(10):
    for y in range(10):
        for z in [""] + [str(n) for n in range(100)]:
            num = int(f"523{x}0{y}3{z}8")
            if num % 1891 == 0:
                print(num, num // 1891)