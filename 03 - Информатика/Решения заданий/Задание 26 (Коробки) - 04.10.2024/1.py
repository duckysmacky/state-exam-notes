file = open("1.txt")
N = int(file.readline())
boxes = sorted(list(map(int, file.readlines())), reverse=True)
gifts = [boxes.pop(0)]
for box in boxes:
    if gifts[-1] - box >= 5:
        gifts.append(box)
print(len(gifts), min(gifts))