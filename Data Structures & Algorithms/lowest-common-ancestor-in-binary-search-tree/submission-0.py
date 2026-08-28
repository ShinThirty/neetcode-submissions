# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lca(self, root, p, q):
        if p == root or q == root or p.val < root.val < q.val:
            return root
        
        if q.val < root.val:
            return self.lca(root.left, p, q)
        else:
            return self.lca(root.right, p, q)


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        return self.lca(root, p, q)