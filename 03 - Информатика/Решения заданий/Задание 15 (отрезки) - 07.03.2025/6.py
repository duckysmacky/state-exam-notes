Q = range(18, 31)
P = range(5, 17)
A = []

for x in range(1, 100):
    f = ((x in P) or (x in Q)) <= (x in A)
    if not f:
        A.append(x)

print(A)
