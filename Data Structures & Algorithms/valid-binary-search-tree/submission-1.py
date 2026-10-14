# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _is_valid_bst(self, root):
        if root is None:
            return True, None, None

        left_valid, left_min, left_max = self._is_valid_bst(root.left)
        right_valid, right_min, right_max = self._is_valid_bst(root.right)

        order_valid = (left_max is None or left_max < root.val) and (right_min is None or root.val < right_min)
        valid = left_valid and right_valid and order_valid
        cur_min = left_min if left_min is not None else root.val
        cur_max = right_max if right_max is not None else root.val
        return valid, cur_min, cur_max

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid, _, _ = self._is_valid_bst(root)
        return valid