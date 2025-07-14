#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        output=[]
        for i,num in enumerate(numbers):
            compliment=target-num
            if compliment in seen:
                output=[seen[compliment]+1, i+1]
                if compliment>num:
                    output=[i+1,seen[compliment]+1]
            seen[num]=i
        return output
# @lc code=end

