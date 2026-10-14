# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_val_to_idx = {val: idx for idx, val in enumerate(inorder)}

        preId = 0

        def dfs(inStart, inEnd) -> TreeNode:
            if inEnd < inStart:
                return None
            
            nonlocal preId
            root_val = preorder[preId]
            preId += 1
            root = TreeNode(root_val)
            inId = inorder_val_to_idx[root_val]
            root.left = dfs(inStart, inId - 1)
            root.right = dfs(inId + 1, inEnd)

            return root
        
        return dfs(0, len(inorder) - 1)
