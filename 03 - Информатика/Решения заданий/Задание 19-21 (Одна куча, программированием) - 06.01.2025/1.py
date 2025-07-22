def go(S: int, target: int, step: int, win_steps: list) -> bool:
    if S >= target and step in win_steps:
        return True
    if S >= target and step not in win_steps:
        return False
    if S < target and step == max(win_steps):
        return False
    if (step + 1) % 2 == win_steps[0] % 2:
        return go(S + 1, target, step + 1, win_steps) or go(S * 3, target, step + 1, win_steps)
    else:
        return go(S + 1, target, step + 1, win_steps) and go(S * 3, target, step + 1, win_steps)

for S in range(1, 55 + 1):
    if go(S, 56, 0, [2, 4]) and not go(S, 56, 0, [2]):
        print(S)