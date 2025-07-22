Q = range(20, 40)
P = range(10, 25)
A = []

for x in range(1, 100):
    f = ((x in P) and (x not in Q)) <= (x in A)
    if not f:
        A.append(x)

print(A)
