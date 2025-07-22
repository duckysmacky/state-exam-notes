file = open("3.txt")
total = int(file.readline())
boxes = []
for line in file:
    size, color = line.split()
    boxes.append([int(size), color])
boxes.sort(reverse=True)
blocks = []
while len(boxes) != 0:
    gifts = [boxes.pop(0)]
    for box in boxes[:]:
        size_b, color_b = box
        size_g, color_g = gifts[-1]
        if size_g - size_b >= 8 and color_g != color_b:
            gifts.append(box)
            boxes.remove(box)
    blocks.append(gifts)
print(len(blocks), len(max(blocks, key=len)))