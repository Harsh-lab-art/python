class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            bit = nums[i][i]
            res.append("1" if bit == "0" else "0")
            
        return "".join(res)
        
