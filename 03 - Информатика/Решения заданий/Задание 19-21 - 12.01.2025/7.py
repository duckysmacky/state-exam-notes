def go(S: int, step: int, win_steps: tuple) -> bool:
    goal = 155
    if S >= goal: return step in win_steps
    if S < goal and step == max(win_steps): return False
    moves = [go(S + 4, step + 1, win_steps), go(S * 2, step + 1, win_steps)]
    return any(moves) if (step + 1) % 2 == win_steps[0] % 2 else all(moves)

play = lambda *s: print([S for S in range(1, 140) if go(S, 0, s)])
play(2)
play(3)
play(2, 4)