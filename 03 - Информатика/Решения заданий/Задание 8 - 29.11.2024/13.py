from itertools import product

for i, word in enumerate(product(sorted("ДРАЙВЕ"), repeat=5), start=1):
    word = ''.join(word)
    if word == ''.join(sorted(word, reverse=True)) and len(set(word)) >= 3 \
        and all(f"{l}В" not in word for l in "ДРЙВ") and all(f"В{l}" not in word for l in "РЙВР"):
        print(i)
        break