def sliding_window(nums, k):
    max_sum = float('-inf')
    current_sum = 0

    if len(nums) < k:
        print(f'No subarray of {k}')
        return;

    for i in range(k):
        current_sum += nums[i]

    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

print(sliding_window([1, 2, 6, 2, 4, 1], 3))
print(sliding_window([100, 200, 300, 400], 2))
# print(sliding_window([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
# print(sliding_window([1, 4, 2], 4))