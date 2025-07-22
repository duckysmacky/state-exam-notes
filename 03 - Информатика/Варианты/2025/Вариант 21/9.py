file = open('9.txt')

def is_triangle(nums):
    return sum(x == 90 for x in nums) == 1 and sum(nums) == 180

cnt = 0
for line in file:
    nums = list(map(int, line.split()))
    if is_triangle(nums):
        print(nums)
        cnt += 1
print(cnt)