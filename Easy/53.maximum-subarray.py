class Solution:
    def maxSubArray(self,nums:List[int]) -> int:
        total=0
        temp=0
        for i in nums:
            temp=temp+i
            if temp<0:
                temp=0
                continue
            else:
                if temp>total:
                    total=temp
        return total
                    