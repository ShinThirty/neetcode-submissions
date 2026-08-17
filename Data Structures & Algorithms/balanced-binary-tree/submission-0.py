# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0
        else:
            lh = self.height(root.left)
            rh = self.height(root.right)
            if lh < rh:
                lh, rh = rh, lh
            diff = lh - rh
            if self.balanced:
                self.balanced = diff <= 1
            return 1 + lh

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.height(root)
        return self.balanced
        