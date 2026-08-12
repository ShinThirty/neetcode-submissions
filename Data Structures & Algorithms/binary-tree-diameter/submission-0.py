# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode | None):
        if not root:
            return 0
        else:
            ld, rd = self.dfs(root.left), self.dfs(root.right)
            self.diameter = max(self.diameter, ld + rd)
            return 1 + max(ld, rd)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter
        