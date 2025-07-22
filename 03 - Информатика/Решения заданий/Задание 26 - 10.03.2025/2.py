file = open("2.txt")
n_files, k_disks = map(int, file.readline().split())
disks = [0] * k_disks
files = [list(map(int, line.split())) for line in file]
files.sort()

cnt, last = 0, -1
for start, end in files:
    for i in range(k_disks):
        if start > disks[i]:
            disks[i] = end
            cnt += 1
            last = i + 1
            break
print(cnt, last)
