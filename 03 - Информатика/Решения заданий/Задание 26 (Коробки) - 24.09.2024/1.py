file = open("1.txt")
total = int(file.readline())
boxes = sorted(list(map(int, file.readlines())), reverse=True)
gifts = [boxes[0]]
for box in boxes[1:]:
    if gifts[-1] - box >= 5:
        gifts.append(box)
print(len(gifts), min(gifts))