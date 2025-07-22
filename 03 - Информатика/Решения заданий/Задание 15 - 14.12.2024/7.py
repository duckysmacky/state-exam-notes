Q = range(18, 35)
P = range(2, 17)
A = []
for x in range(1, 100):
    f = ((x in P) or (x in Q)) <= (x in A)
    if not f:
        A.append(x)
print(A)
