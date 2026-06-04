class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        right=1
        maxlen=0
        length=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            length=(right-left+1)
            maxlen=max(maxlen, length)
        return maxlen