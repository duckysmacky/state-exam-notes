from functools import lru_cache

@lru_cache
def walk(start, finish, point, last):
    if start >= finish: return start == finish and point == 1
    if start == 18: point = 1
    if start == 33: point = 0
    res = walk(start + 1, finish, point, 0) + walk(start + 3, finish, point, 0)
    if last == 0: res += walk(start * 2, finish, point, 1)
    return res

print(walk(2, 51, 0, 0))
