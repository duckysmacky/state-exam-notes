def go(S, step, win_steps):
    goal = 202
    if S > goal: return step in win_steps
    if S < goal and step == max(win_steps): return False
    moves = [
        go(S + 1, step + 1, win_steps),
        go(S + 4, step + 1, win_steps),
        go(S * 3, step + 1, win_steps)
    ]
    return any(moves) if (step + 1) % 2 == max(win_steps) % 2 else all(moves)

play = lambda *s: [S for S in range(1, 202) if go(S, 0, s)]
print(play(2))
print(play(3))
print(play(2, 4))
