#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        list=[]
        if x==1 or x==0:
            return True
        elif x>1:
            while x>=1:
                temp=x//10
                list.append(x-temp*10)
                x=temp
            return list==list[::-1]
        else:
            return False
        
# @lc code=end

