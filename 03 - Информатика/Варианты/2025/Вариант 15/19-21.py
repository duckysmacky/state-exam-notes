def go(N, S, step, win_steps):
    goal = 178
    stones = N + S
    if stones >= goal: return step in win_steps
    if stones < goal and step == max(win_steps): return False
    moves = [
        go(N + 4, S, step + 1, win_steps), go(N, S + 3, step + 1, win_steps),
        go(N * 2, S, step + 1, win_steps), go(N, S * 3, step + 1, win_steps)
    ]
    return any(moves) if (step + 1) % 2 == win_steps[0] % 2 else all(moves)

play = lambda *s: [S for S in range(1, 157) if go(21, S, 0, s)]
play(2)
print(sum(play(3)))
print([x for x in play(1, 3, 5) if x not in play(1, 3)])
