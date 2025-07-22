number_range = range(164361, 164423 + 1)
test_range = range(50, 54 + 1)
ans = []


def find_pair(x: int) -> (int, int):
    pairs = set()
    for a in range(1, int(x ** 0.5) + 1):
        for b in range(a, int(x ** 0.5) + 1):
            if a ** 2 + b ** 2 == x:
                if (a, b) not in pairs:
                    pairs.add((a, b))
    if len(pairs) == 1:
        print(pairs.pop())


for n in number_range:
    find_pair(n)
