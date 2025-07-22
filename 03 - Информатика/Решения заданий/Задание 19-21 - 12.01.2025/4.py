def go(N: int, S: int, step: int, win_steps: tuple) -> bool:
    goal = 65
    stones = N + S
    if stones >= goal: return step in win_steps
    if stones < goal and step == max(win_steps): return False
    moves = [go(N + 2, S, step + 1, win_steps), go(N * 2, S, step + 1, win_steps),
             go(N, S + 2, step + 1, win_steps), go(N, S * 2, step + 1, win_steps)]
    return any(moves) if (step + 1) % 2 == win_steps[0] % 2 else all(moves)

play = lambda *s: [S for S in range(1, 61) if go(3, S, 0, s)]
print(play(1))
print(play(3))
print(play(2))
print(play(2, 4))