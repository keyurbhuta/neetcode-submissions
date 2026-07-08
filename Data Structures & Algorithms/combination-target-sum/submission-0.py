class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        final=[]
        def dfs(i, total):
            if total==target:
                final.append(res[:])
                return
            if i==len(nums) or total>target:
                return
            res.append(nums[i])
            dfs(i, total+nums[i])
            res.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return final
