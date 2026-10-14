# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        working_list = []

        def dfs(node):
            nonlocal working_list
            if node is None:
                working_list.append('N')
            else:
                working_list.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return '#'.join(working_list)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        working_list = data.split('#')
        idx = -1
        def dfs():
            nonlocal working_list, idx
            idx += 1
            cur_val = working_list[idx]

            if cur_val == 'N':
                return None
            else:
                node = TreeNode(int(cur_val))
                node.left = dfs()
                node.right = dfs()
                return node
        
        return dfs()
