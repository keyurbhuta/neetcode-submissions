class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def h(n):
            if not n:
                return 0
            l, r = h(n.left), h(n.right)
            return -1 if l < 0 or r < 0 or abs(l - r) > 1 else 1 + max(l, r)

        return h(root) >= 0