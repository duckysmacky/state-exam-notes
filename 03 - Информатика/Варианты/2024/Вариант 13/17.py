file = open("Задание 17/17.txt")
data = list(map(int, file.readlines()))

nums = []
for num in data:
    if num % 2 == 0 and num % 3 != 0:
        nums.append(num)
nums.sort(reverse=True)
print(len(nums), nums[:3])
