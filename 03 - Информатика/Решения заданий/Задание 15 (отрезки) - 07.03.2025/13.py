P = range(20, 151)
Q = range(40, 101)
R = range(30, 121)
S = range(10, 81)
T = range(60, 201)
U = range(90, 171)
A = []
for x in range(0, 1001):
    f = (((x in P) and (x in Q)) or ((x not in A) <= (((x in R) and (x in S)) or ((x in T) and (x in U)))))
    if not f:
        A.append(x)
print(A)
