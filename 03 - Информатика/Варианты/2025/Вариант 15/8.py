from itertools import product

for i, word in enumerate(product(sorted("АЛГОРИТМ"), repeat=5), start=1):
    if i % 2 != 0 and word[0] != 'Т' and word.count('Г') == 2:
        print(i, ''.join(word))
