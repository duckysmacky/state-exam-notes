R = range(12, 31)
Q = range(8, 16)
P = range(10, 21)
A = []

for x in range(1, 100):
    f = ((x in A) or (x in P)) or ((x in Q) <= (x in R))
    if not f:
        A.append(x)

print(A)
