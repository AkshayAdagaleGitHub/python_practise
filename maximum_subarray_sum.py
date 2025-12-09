from typing import List

'''
Input: nums = [2, 3, -2, 4]  
Output: 7  
Explanation: Maximum sum is 2 + 3 + (-2) + 4 = 7.

Input: nums = [1, -1, -5, -4]  
Output: -1  
Explanation: The maximum sum is -1, which is the single element with the highest value.
'''
def max_subarray_sum(nums: List[int]) -> int:
    if not nums:
        return 0

    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current

    return max_global


print(max_subarray_sum([2, 3, -2, 4])) # 7
print(max_subarray_sum([1, -1, -5, -4])) # 1