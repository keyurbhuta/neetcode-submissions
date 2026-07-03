class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxsub = s[0]
        # Odd length palindromes
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > len(maxsub):
                        maxsub = s[left:right+1]
                else:
                    break
                left -= 1
                right += 1

        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > len(maxsub):
                        maxsub = s[left:right+1]
                else:
                    break
                left -= 1
                right += 1
        return maxsub