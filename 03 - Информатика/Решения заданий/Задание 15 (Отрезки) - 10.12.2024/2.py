Q = range(12, 29 + 1)
P = range(5, 41 + 1)
A = []
for x in range(1, 100):
    f = ((x in A) and (x in P)) or not (x in Q)
    if not f:
        A.append(x)
print(A)
print(29 - 12)
