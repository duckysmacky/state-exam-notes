Q = range(17, 91 + 1)
P = range(10, 47 + 1)
A = []

for x in range(1, 100):
    f = ((x in P) and (x in Q)) <= (x in A)
    if not f:
        A.append(x)
print(A)
print(47 - 17)
