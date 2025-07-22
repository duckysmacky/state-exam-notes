file = open("26.txt")
n_files, m_size = map(int, file.readline().split())
photos, videos = [], []
for line in file:
    val = int(line)
    if val <= 100:
        photos.append(val)
    else:
        videos.append(val)
photos.sort()
videos.sort()

added, cnt = [], 0
flash = 0
while flash < m_size / 2:
    flash += videos.pop(0)
    cnt += 1
for photo in photos:
    if flash == 524189:
        print(max([x for x in photos if flash + x <= m_size]))
    if flash + photo <= m_size:
        print(flash, photo)
        flash += photo
        added.append(photo)
        cnt += 1
    else:
        break

print(cnt)
