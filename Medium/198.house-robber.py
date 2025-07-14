#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # total1=0
        # total2=0
        # for i,num in enumerate(nums):
        #     if i%2==0:
        #         total2=total2+num
        #     else:
        #         total1=total1+num
        # return max(total1,total2)
        rob1,rob2=0,0
        for n in nums:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
# @lc code=end

