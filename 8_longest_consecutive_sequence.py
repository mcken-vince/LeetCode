## 128. Longest Consecutive Sequence
from testing import test

def longestConsecutive(nums):
  longestSeq = 0
  currentSeq = 1
  prev = None
  for n in sorted(nums):
    if prev != None and n - 1 == prev:
      currentSeq += 1
    else:
      currentSeq = 1
    
    if currentSeq > longestSeq:
      longestSeq = currentSeq
      
    prev = n  
  return longestSeq


nums = [100,4,200,1,3,2]
test(longestConsecutive, 4, nums)

nums = [0,3,7,2,5,8,4,6,0,1]
test(longestConsecutive, 9, nums)