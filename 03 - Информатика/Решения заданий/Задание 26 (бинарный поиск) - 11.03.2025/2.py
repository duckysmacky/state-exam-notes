def binary_search(arr, target):
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

file = open("2.txt")
n = int(file.readline())
nums = sorted(list(map(int, file.readlines())))
cnt, max_avg = 0, 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] % 2 != 0 and nums[j] % 2 != 0:
            pair = (nums[i], nums[j])
            avg = sum(pair) // len(pair)
            if binary_search(nums, avg):
                cnt += 1
                max_avg = max(max_avg, avg)
print(cnt, max_avg)
