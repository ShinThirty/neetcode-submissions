# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        res = []
        if root is not None:
            queue.append(root)
        
        while queue:
            length = len(queue)
            added = False
            for _ in range(length):
                cur = queue.popleft()
                if not added:
                    res.append(cur.val)
                    added = True
                if cur.right is not None:
                    queue.append(cur.right)
                if cur.left is not None:
                    queue.append(cur.left)
        
        return res
        