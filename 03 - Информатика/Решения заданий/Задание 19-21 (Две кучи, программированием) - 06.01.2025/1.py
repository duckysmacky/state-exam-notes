def go(N: int, S: int, step: int, *win_steps: int) -> bool:
    target = 89
    stones = N + S
    if stones >= target and step in win_steps:
        return True
    if stones >= target and step not in win_steps:
        return False
    if stones < target and step == max(win_steps):
        return False
    if (step + 1) % 2 == win_steps[0] % 2:
        return any([go(N + 2, S, step + 1, *win_steps), go(N, S + 2, step + 1, *win_steps),
                go(N * 3, S, step + 1, *win_steps), go(N, S * 3, step + 1, *win_steps)])
    else:
        return all([go(N + 2, S, step + 1, *win_steps), go(N, S + 2, step + 1, *win_steps),
                    go(N * 3, S, step + 1, *win_steps), go(N, S * 3, step + 1, *win_steps)])

for S in range(1, 78 + 1):
    if go(10, S, 0, 2, 4) and not go(10, S, 0, 2):
        print(S)