from fnmatch import fnmatch

def cnt_divs(x: int) -> int:
    def is_prime(x: int) -> bool:
        for div in range(2, int(x ** 0.5) + 1):
            if x % div == 0:
                return False
        return True
    
    cnt = 0
    for div in range(2, int(x ** 0.5) + 1):
        if is_prime(div):
            if x * x == div:
                cnt += 1
                continue
            elif x % div == 0:
                cnt += 1
                if is_prime(x // div):
                    cnt += 1
    return cnt

for num in range(74, 10 ** 9, 74):
    if fnmatch(str(num), "5*1?*1?*") and num % 74 == 0 and num % 13 != 0:
        cnt = cnt_divs(num) 
        if cnt >= 6: 
            print(num, cnt)
            break