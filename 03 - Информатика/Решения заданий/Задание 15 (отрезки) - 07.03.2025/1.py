Q = range(7, 16)
P = range(6, 17)
A = []

for x in range(1, 100):
    f = ((x in P) or not (x in A)) and ((x not in Q) or (x in A))
    if not f:
        A.append(x)

print(A)
