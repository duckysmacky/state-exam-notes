def go(S: int, step: int, win_steps: tuple) -> bool:
    goal = 101
    if S >= 101: return step in win_steps
    if S < 101 and step == max(win_steps): return False
    moves = [go(S + 2, step + 1, win_steps), go(S * 2, step + 1, win_steps)]
    return any(moves) if (step + 1) % 2 == win_steps[0] % 2 else all(moves)

play = lambda *steps: [S for S in range(1, 101) if go(S, 0, steps)]
print(play(2))
print(play(3))
print(play(2, 4))