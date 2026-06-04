class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        maxcount=0
        for num in nums:
            seen.add(num)
        for num in nums:
            if num-1 not in seen:
                count=1
                curr=num
                while curr+1 in seen:
                    count+=1
                    curr+=1
                maxcount=max(maxcount, count)
        return maxcount