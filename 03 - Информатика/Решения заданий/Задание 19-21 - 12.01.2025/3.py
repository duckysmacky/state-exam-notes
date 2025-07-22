def go(S: int, step: int, win_steps: tuple) -> bool:
    goal = 46
    if S >= goal: return step in win_steps
    if S < goal and step == max(win_steps): return False
    moves = [go(S + 2, step + 1, win_steps), go(S * 2, step + 1, win_steps)]
    return any(moves) if (step + 1) % 2 == win_steps[0] % 2 else all(moves)

play = lambda *s: [S for S in range(1, 45) if go(S, 0, s)]

print(play(2))
print(play(3))
print(play(2, 4))