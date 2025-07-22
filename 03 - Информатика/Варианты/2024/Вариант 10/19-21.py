def go(N: int, S: int, step: int, win_steps: tuple) -> bool:
    goal = 125
    stones = N + S
    if stones >= goal: return step in win_steps
    if stones < goal and step == max(win_steps): return False
    moves = [
        go(N + 1, S, step + 1, win_steps), go(N * 4, S, step + 1, win_steps),
        go(N, S + 1, step + 1, win_steps), go(N, S * 4, step + 1, win_steps)
    ]
    return any(moves) if (step + 1) % 2 == win_steps[0] % 2 else all(moves)

play = lambda *s: print([S for S in range(1, 118) if go(7, S, 0, s)])
play(2)
play(3)
play(2, 4)
