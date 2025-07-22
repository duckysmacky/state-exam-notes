from itertools import product

def valid(codes: list, check_code: str) -> bool:
    return not any(check_code.startswith(code) or code.startswith(check_code) for code in codes)

letter_codes = ["00", "011", "11", "101"]
possible_codes = [''.join(code) for n in range(1, 6) for code in product("01", repeat=n)]
valid_codes = [code for code in possible_codes if valid(letter_codes, code)]
print(valid_codes)
