def find(start: int, end: int) -> int:
    if start > end: return 0
    if start == end: return 1
    if start == 11: return 0
    return find(start + 1, end) + find(start * 2, end)

print(find(2, 16) * find(16, 34))