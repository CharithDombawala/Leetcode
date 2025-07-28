#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=''.join(c for c in s if c.isalnum()).lower()
        return cleaned==cleaned[::-1]

        
# @lc code=end

