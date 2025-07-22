def find(start, end):
    if start == 5: return 0
    if start > end: return 0
    if start == end: return 1
    return find(start + 1, end) + find(start * 3, end)
print(find(1, 21))