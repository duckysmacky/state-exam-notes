def go(N: int, S: int, step: int, win_steps: tuple) -> bool:
    target = 80
    stones = N + S
    if stones >= target: return step in win_steps
    if stones < target and step == max(win_steps): return False
    moves = [
        go(N + 1, S, step + 1, win_steps), go(N * 3, S, step + 1, win_steps),
        go(N, S + 1, step + 1, win_steps), go(N, S * 3, step + 1, win_steps)
    ]
    return any(moves) if (step + 1) % 2 == win_steps[0] % 2 else all(moves)

def play(*win_steps: int) -> list:
    N = 3
    return [S for S in range(1, 76 + 1) if go(N, S, 0, win_steps)]

print(play(2))
print(play(3))
print(play(2, 4))