def alg(s: str) -> str:
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "12>", 1)
        if ">2" in s:
            s = s.replace(">2", "5>", 1)
        if ">0" in s:
            s = s.replace(">0", "22>", 1)
    return s


def check(x: int) -> bool:
    if x < 2:
        return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True


for n in range(1000):
    s = ">" + 56 * "0" + 49 * "1" + n * "2"
    result = alg(s).replace(">", "")
    if check(sum(map(int, result))):
        print(n)
        break