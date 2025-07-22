def find(start: int, end: int) -> int:
    if start < end: return 0
    if start == end: return 1
    return find(start - 2, end) + find(start // 2, end)
print(find(52, 14) * find(14, 2))
