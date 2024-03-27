## 347. Top K Frequent Elements
from testing import test

def topKFrequent(nums, k):
  freqMap = {}
  for n in nums:
    if n in freqMap:
      freqMap[n] += 1
    else:
      freqMap[n] = 1
  sortedFreqMap = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)
  print(sortedFreqMap)
  return [n for n, freq in sortedFreqMap[0:k]]


nums, k = [1,1,1,2,2,3], 2
test(topKFrequent, [1,2], nums, k)

nums, k = [1], 1
test(topKFrequent, [1], nums, k)
