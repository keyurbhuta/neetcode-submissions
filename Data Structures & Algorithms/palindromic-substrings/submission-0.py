class Solution:
    def countSubstrings(self, s: str) -> int:  
        res=0
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:                   
                    res+=1
                else:
                    break
                left -= 1
                right += 1
        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    res+=1
                else:
                    break
                left -= 1
                right += 1
        return res