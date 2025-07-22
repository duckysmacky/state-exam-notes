Q = range(8, 16 + 1)
P = range(12, 28 + 1)
A = list(range(1, 100))
for x in range(1, 100):
    f = (x in A) <= ((x in P) and not (x in Q))
    if not f:
        A.remove(x)
print(A)
print(28 - 16)
