# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            if left<0:
                left=0
            if right<0:
                right=0
            path_sum=root.val+left+right
            self.max_path_sum=max(self.max_path_sum, path_sum)
            max_gain=root.val+max(left, right)
            return max_gain
        dfs(root)
        return self.max_path_sum