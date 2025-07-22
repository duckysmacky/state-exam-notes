def find(start, end):
    if start == 19: return 0
    if start > end: return 0
    if start == end: return 1
    return find(start + 1, end) + find(start * 2, end)
print(find(2, 10) * find(10, 29))