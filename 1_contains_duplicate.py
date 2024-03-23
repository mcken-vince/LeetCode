## 217. Contains Duplicate
from testing import test

# def containsDuplicate(nums):
#   uniqueItems = []
#   for n in nums:
#     if n not in uniqueItems:
#       uniqueItems.append(n)
#   return len(uniqueItems) != len(nums)
    

def containsDuplicate(nums):
  uniqueNums = set(nums)
  return len(uniqueNums) != len(nums)


nums = [1,2,3,1]
test(containsDuplicate, True, nums)

nums = [1,2,3,4]
test(containsDuplicate, False, nums)

nums = [1,1,1,3,3,4,3,2,4,2]
test(containsDuplicate, True, nums)
