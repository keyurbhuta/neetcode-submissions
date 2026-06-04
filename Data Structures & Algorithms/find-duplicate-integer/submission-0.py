class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sum=0
        nums=sorted(nums)
        for i in range(1, len(nums)+1):
            if nums[i]==nums[i-1]:
                return nums[i]
