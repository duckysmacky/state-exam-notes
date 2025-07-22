from functools import lru_cache



@lru_cache
def find(start, end, buff):
    if sorted(list(buff)) != list(buff): return 0
    if start > end: return 0
    if start == end: return 1
    return find(start * 3, end, buff + '1') + find(start * 2, end, buff + '2') + find(start + 2, end, buff + '3') + find(start + 1, end, buff + '4')
print(find(2, 25, ""))