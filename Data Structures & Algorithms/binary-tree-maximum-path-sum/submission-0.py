# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        running_max = -float('inf')

        def max_path_sum(node):
            if node is None:
                return 0

            nonlocal running_max

            left_max = max(0, max_path_sum(node.left))
            right_max = max(0, max_path_sum(node.right))

            candidate = left_max + node.val + right_max
            running_max = max(running_max, candidate)

            return max(left_max, right_max) + node.val
        
        max_path_sum(root)

        return running_max