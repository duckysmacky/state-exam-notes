def alg(n: int) -> int:
    n = str(n)
    sums = [int(n[i]) + int(n[i + 1]) for i in range(len(n) - 1)]
    print(sums)
    sums.sort(reverse=True)
    sums.pop(0)
    return int(''.join(map(str, sums)))

for n in range(1000, 9999 + 1):
    if alg(n) == 127:
        print(n)
