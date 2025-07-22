file = open("9.txt")

june = []
for line in file:
    data, *nums = line.split()
    nums = list(map(float, nums))
    month = data.split('/')[0]
    if month == '5':
        for num in nums:
            if num > 25:
                june.append(num)
avg = sum(june) / len(june)
print(avg)
