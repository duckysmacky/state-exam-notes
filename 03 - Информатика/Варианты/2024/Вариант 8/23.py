def travel(start, finish, found):
    if start >= finish: return start == finish and found == 1
    if start == 12: found = 1
    return travel(start + 1, finish, found) + travel(start + 7, finish, found)

print(travel(5, 26, 0))