class Solution(object):
    def maxSum(self, nums):
        unique=set(nums)
        sum=0
        pos=False
        for num in unique:
            if num>0:
                sum+=num
                pos=True
        if pos:
            return sum
        return max(unique)            
