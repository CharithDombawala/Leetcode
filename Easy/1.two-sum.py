#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# @lc code=start

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
    
# @lc code=end

