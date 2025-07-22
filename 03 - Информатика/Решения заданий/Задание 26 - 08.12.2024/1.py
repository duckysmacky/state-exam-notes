file = open("1.txt")
file_count, disk_count = map(int, file.readline().split())
files = sorted([list(map(int, line.split())) for line in file])
disks = [0] * disk_count
cnt, last_disk = 0, 0

for start, end in files:
    for i in range(disk_count):
        if start > disks[i]:
            disks[i] = end
            cnt += 1
            last_disk = i + 1
            break
print(cnt, last_disk)