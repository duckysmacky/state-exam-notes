from itertools import permutations

cnt = 0
glas = 'ОИ'
sogl = 'ПРБНК'
for word in set(permutations('ПРОБНИК')):
    word = ''.join(word).replace('О', 'И')
    if word[0] in sogl and word[-1] in sogl and 'ИИ' not in word:
        print(word)
        cnt += 1
print(cnt)