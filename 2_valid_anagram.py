## 242. Valid Anagram
from testing import test

def isAnagram(s, t):
  def sort(str):
    char_list = sorted(list(str))
    return ''.join(char_list)
  
  return sort(s) == sort(t)



args = ("anagram", "nagaram")
test(isAnagram, True, *args)

args = ("rat", "car")
test(isAnagram, False, *args)