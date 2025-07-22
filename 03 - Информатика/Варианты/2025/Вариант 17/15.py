P = range(10, 31)
Q = range(25, 56)
A = list(range(1, 100))
for x in range(1, 100):
    f = (x in A) <= ((x in P) or (x in Q))
    if not f: A.remove(x)
print(A)
