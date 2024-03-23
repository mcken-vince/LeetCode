## 49. Group Anagrams
from testing import test

def groupAnagrams(strs):
  anagramGroups = {}
  for s in strs:
    sortedS = ''.join(sorted(s))
    if sortedS in anagramGroups:
      anagramGroups[sortedS].append(s)
    else:
      anagramGroups[sortedS] = [s]
  return [group for group in anagramGroups.values()]



strs = ["eat","tea","tan","ate","nat","bat"]
test(groupAnagrams, [["bat"],["nat","tan"],["ate","eat","tea"]], strs)

strs = [""]
test(groupAnagrams, [[""]], strs)

strs = ["a"]
test(groupAnagrams, [["a"]], strs)
