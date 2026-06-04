class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        window = {}

        required = len(target)
        formed = 0

        left = 0
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in target and window[ch] == target[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]

                if left_char in target and window[left_char] == target[left_char]:
                    formed -= 1

                window[left_char] -= 1
                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]