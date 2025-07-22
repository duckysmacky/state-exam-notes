from time import sleep

file = open("Задание 26/26-v2.txt")
atms, clients = map(int, file.readline().split())
queue = []
for line in file:
    start_time, time = map(int, line.split())
    queue.append([start_time, start_time + time, time])

queue.sort()

current_time = queue[0][0]
end_of_day_time = 24 * 60
occupied = []
client_n = 0

while current_time < end_of_day_time:
    while len(occupied) < atms:
        start, end, time = queue[0]
        if current_time >= start:
            client_n += 1
            print(f"Added customer #{client_n} {queue[0]}")
            occupied.append(queue.pop(0))
        else:
            break
    if len(occupied) > 0 and current_time >= occupied[0][1]:
        print(f"Removed customer #{client_n} {occupied[0]}")
        occupied.pop(0)
    current_time += 1

print(current_time)
print(client_n)
print(occupied)