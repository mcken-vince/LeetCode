## 125. Valid Palindrome
from testing import test

def is_palindrome(s):
  str = ''.join(char for char in s if char.isalnum()).lower()
  return str == str[::-1]  

test(is_palindrome, True, "A man, a plan, a canal: Panama")
test(is_palindrome, False, "race a car")
test(is_palindrome, True, " ")