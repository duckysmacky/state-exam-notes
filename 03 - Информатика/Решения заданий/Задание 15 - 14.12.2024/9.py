def trg(n, m, k) -> bool:
    return (n + m > k) and (m + k > n) and (k + n > m)

def max(a, b) -> int:
    return a if a > b else b

for A in range(1, 1000):
    for x in range(1, 1000):
        f = not ((trg(x, 11, 24) == (not (max(x, 7) > 32))) and trg(x, A, 7))
        if not f: break
    else:
        print(A)
