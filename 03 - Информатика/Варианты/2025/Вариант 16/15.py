def triangle(n, m, k):
    positive = n > 0 and m > 0 and k > 0
    exists = n + m > k and m + k > n and k + n > m
    return positive and exists

for A in range(1, 1000):
    for x in range(1, 10_000):
        f = not ((triangle(x, 11, 18) == (not (max(x, 5) > 15))) and triangle(x, A, 5))
        if not f:
            break
    else:
        print(A)
