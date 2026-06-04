class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        maxf = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]

            if ch not in freq:
                freq[ch] = 0

            freq[ch] += 1

            maxf = max(maxf, freq[ch])

            while (right - left + 1) - maxf > k:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans