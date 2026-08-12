# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def DFS(node):
            if not node:
                return TreeNode(val)
            
            if node.val > val:
                if not node.left:
                    node.left = DFS(node.left)
                else:
                    DFS(node.left)
    
            elif node.val < val:
                if not node.right:
                    node.right = DFS(node.right)
                else:
                    DFS(node.right)

            return node
        
        root = DFS(root)
        return root