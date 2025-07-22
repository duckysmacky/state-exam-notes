R = range(38, 95)
Q = range(50, 63)
P = range(27, 131)
A = []

for x in range(1, 200):
    f = ((x not in P) or (x in Q)) or ((x not in A) <= (x not in R))
    if not f:
        A.append(x)

print(A)
