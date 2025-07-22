file = open("2.txt")
total = int(file.readline())
boxes = sorted(list(map(int, file.readlines())), reverse=True)
blocks = []
while len(boxes) != 0:
    gifts = [boxes.pop(0)]
    for box in boxes[:]:
        if gifts[-1] - box >= 5:
            gifts.append(box)
            boxes.remove(box)
    blocks.append(gifts)
print(len(blocks), len(blocks[0]))