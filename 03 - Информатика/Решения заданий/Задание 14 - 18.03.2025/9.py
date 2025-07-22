def base(x, p):
    nums = []
    while x > 0:
        nums.append(x % p)
        x //= p
    return nums

val = 3 * 5103 ** 2020 + 3 * 729 ** 2021 - 2 * 343 ** 2022 + 27 ** 2023 - 4 * 7 ** 2024 - 2029
val28 = base(val, 28)
print(sum(1 for x in val28 if x > 15))
