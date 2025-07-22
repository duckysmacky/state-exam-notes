file = open("4.txt")
N = int(file.readline())
boxes = []
for line in file:
    size, color = line.split()
    boxes.append([int(size), color])
boxes.sort(reverse=True)
blocks = []
while len(boxes) > 0:
    gift = [boxes.pop(0)]
    for box in boxes[:]:
        if gift[-1][0] - box[0] >= 8 and gift[-1][1] != box[1]:
            gift.append(box)
            boxes.remove(box)
    blocks.append(gift)
print(len(blocks), len(max(blocks, key=len)))