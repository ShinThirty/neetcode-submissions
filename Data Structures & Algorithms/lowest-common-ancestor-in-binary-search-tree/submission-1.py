# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        cur = root
        while True:
            if p == cur or q == cur or p.val < cur.val < q.val:
                return cur
            
            if q.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right