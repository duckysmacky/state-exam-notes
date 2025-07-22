from string import digits, ascii_uppercase
file = open("5.txt")
nums = file.readlines()
alph = digits + ascii_uppercase
cnt = 0
for num in nums:
    syst = alph.index(max(num)) + 1
    if syst in range(2, 14 + 1) and int(num, syst) % 15 == 0:
        cnt += 1
print(cnt)