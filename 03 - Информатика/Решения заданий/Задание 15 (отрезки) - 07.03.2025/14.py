P = range(20, 131)
Q = range(40, 101)
R = range(25, 121)
S = range(50, 151)
A = []
for x in range(1, 100):
    f = ((((x in P) or (x in Q)) and ((x not in A) and (x in R)))) <= (x in S)
    if not f:
        A.append(x)
print(A)
