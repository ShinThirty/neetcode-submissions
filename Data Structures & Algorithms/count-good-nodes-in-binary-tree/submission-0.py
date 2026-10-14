# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def _traverse(self, root: TreeNode, maximum: int):
        if root is None:
            return
        
        if maximum <= root.val:
            self.ans += 1
        
        if root.left is not None:
            self._traverse(root.left, max(maximum, root.left.val))
        if root.right is not None:
            self._traverse(root.right, max(maximum, root.right.val))


    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        if root is not None:
            self._traverse(root, root.val)
        return self.ans