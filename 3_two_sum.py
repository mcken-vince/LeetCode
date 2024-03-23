## 1. Two Sum
from testing import test

def twoSum(nums, target):
  indexedList = sorted([(i, n) for i, n in enumerate(nums)], key=lambda x: x[1])
  i, j = 0, len(indexedList) - 1
  while i < j:
    sum = indexedList[i][1] + indexedList[j][1]
    if sum == target:
      return [indexedList[i][0], indexedList[j][0]]
    elif sum < target:
      i += 1
    else:
      j -= 1




nums, target = [2,7,11,15], 9
test(twoSum, [0, 1], nums, target)
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums, target = [3,2,4], 6
test(twoSum, [1,2], nums, target)

nums, target = [3,3], 6
test(twoSum, [0,1], nums, target)
