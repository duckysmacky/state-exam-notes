R = range(35, 50 + 1)
Q = range(5, 15 + 1)
P = range(10, 40 + 1)
A = []
for x in range(1, 100):
    f = ((x in A) or (x in P)) or ((x in Q) <= (x in R))
    if not f:
        A.append(x)
print(A)
