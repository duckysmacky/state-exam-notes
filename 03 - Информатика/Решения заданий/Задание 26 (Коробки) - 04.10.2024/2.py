file = open("2.txt")
N, M = map(int, file.readline().split())
boxes = []
stripes = []
for _ in range(M):
    box, stripe = map(int, file.readline().split())
    boxes.append(box)
    stripes.append(stripe)
for _ in range(N - M):
    box = int(file.readline())
    boxes.append(box)
boxes.sort(reverse=True)
gift = [boxes.pop(0)]
for box in boxes:
    if gift[-1] - box >= 7 and box in stripes:
        gift.append(box)
print(len(gift), max(gift) - min(gift))