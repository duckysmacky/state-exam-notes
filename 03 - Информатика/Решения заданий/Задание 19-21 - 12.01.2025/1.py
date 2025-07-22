def go(S: int, step: int, win_steps: tuple) -> bool:
    goal = 54
    if S >= goal: return step in win_steps
    if S < goal and step == max(win_steps): return False
    moves = [go(S + 1, step + 1, win_steps),
             go(S + 2, step + 1, win_steps),
             go(S * 3, step + 1, win_steps)]
    is_winner = (step + 1) % 2 == win_steps[0] % 2
    return any(moves) if is_winner else all(moves)

def play(*win_steps: int) -> list:
    return [S for S in range(1, 51) if go(S, 0, win_steps)]

print(play(1))
print(play(3))
print(play(2))
print(play(2, 4))