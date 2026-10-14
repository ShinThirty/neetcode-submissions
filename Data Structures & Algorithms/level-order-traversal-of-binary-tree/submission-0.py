# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = collections.deque()
        if root is not None:
            queue.append(root)

        while queue:
            length = len(queue)
            cur_level = []
            for _ in range(length):
                cur = queue.popleft()
                cur_level.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            res.append(cur_level)
        
        return res
        