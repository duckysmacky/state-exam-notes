from itertools import product

def is_valid(codes: list, code: str) -> bool:
    return not any(c.startswith(code) or code.startswith(c) for c in codes)

letters = ["01", "101", "111", "000", "1101", "0011", "0010"]
possible = [''.join(code) for n in range(1, 6) for code in product("01", repeat=n)]

valid = [code for code in possible if is_valid(letters, code)]
print(valid)
