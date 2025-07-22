P = range(10, 26)
Q = range(28, 41)
A = []

for x in range(1, 100):
    f = ((x in P) and (x not in A)) <= (x not in Q)
    if not f:
        A.append(x)
print(A)
print(len(A))
