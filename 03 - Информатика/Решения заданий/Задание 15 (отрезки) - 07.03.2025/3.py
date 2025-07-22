Q = range(10, 56)
P = range(4, 21)
A = []

for x in range(1, 100):
    f = (x in A) or ((x not in P) <= (x not in Q))
    if not f:
        A.append(x)

print(A)
