# Find the two no. which sum is 6
# Array must be sorted.



nums = [1,2,3,4,5,6,7,8,9]

def two_pointer(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [nums[left], nums[right]]
        elif total > target:
            right -= 1
        else:
            left += 1

    return []

result = two_pointer(nums, 6)
print("Result", result)


