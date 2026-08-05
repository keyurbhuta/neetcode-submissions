class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for _ in range(len(nums))]
        dp[len(nums)-1]=1
        for i in range(len(nums)-1, -1, -1):
            for j in range(1, nums[i]+1):
                if i+j<len(nums) and dp[i+j]==1:
                    dp[i]=1
                    break
        return True if dp[0]==1 else False