# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = 0
        cur = None
        def dfs(root):
            nonlocal order, cur
            if order >= k:
                return
            
            if order < k and root.left is not None:
                dfs(root.left)
            if order < k:
                order += 1
                cur = root
            if order < k and root.right is not None:
                dfs(root.right)
        
        dfs(root)
        return cur.val
        