def binary_search(target, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return False

file = open("1.txt")
n = int(file.readline())
nums = sorted(list(map(int, file.readlines())))
cnt, max_sum = 0, 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] % 2 != nums[j] % 2:
            pair = (nums[i], nums[j])
            if binary_search(sum(pair), nums):
                cnt += 1
                max_sum = max(max_sum, sum(pair))
print(cnt, max_sum)
