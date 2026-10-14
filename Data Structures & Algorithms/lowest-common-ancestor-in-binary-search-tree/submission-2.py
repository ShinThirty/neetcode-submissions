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
        
        lca = root
        while True:
            if p == lca or q == lca or p.val < lca.val < q.val:
                return lca
            
            if q.val < lca.val:
                lca = lca.left
            else:
                lca = lca.right