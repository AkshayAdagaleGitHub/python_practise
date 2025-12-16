
from typing import List

def find_first(array: List[int], num:int) -> int:
    left = 0
    right = len(array) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == num:
            ans = mid
            right = mid - 1
        elif array[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return ans

