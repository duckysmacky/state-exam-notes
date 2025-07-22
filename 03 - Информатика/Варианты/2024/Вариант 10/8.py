from itertools import permutations

sogl = "ПРБНК"
cnt = 0
for word in permutations("ПРОБНИК"):
    if word[0] in sogl and word[-1] in sogl and "ОИ" not in word and "ИО" not in word:
        cnt += 1
print(cnt)
