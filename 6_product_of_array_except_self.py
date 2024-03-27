## 238. Product of Array Except Self
from testing import test

def productExceptSelf(nums):
  n = len(nums)
  left = [1] * n
  right = [1] * n
  for i in range(1, n):
    left[i] = left[i-1] * nums[i-1]
  for i in range(n-2, -1, -1):
    right[i] = right[i+1] * nums[i+1]
  return [left[i] * right[i] for i in range(n)]



test(productExceptSelf, [24, 12, 8, 6], [1, 2, 3, 4])

test(productExceptSelf, [0, 0, 9, 0, 0], [-1,1,0,-3, 3])