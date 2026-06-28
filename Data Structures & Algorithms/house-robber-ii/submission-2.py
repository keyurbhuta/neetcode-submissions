class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(arr):
            arr.append(0)

            for i in range(len(arr) - 4, -1, -1):
                arr[i] += max(arr[i + 2], arr[i + 3])

            return max(arr[0], arr[1])

        return max(
            solve(nums[:-1]),  # exclude last
            solve(nums[1:])    # exclude first
        )