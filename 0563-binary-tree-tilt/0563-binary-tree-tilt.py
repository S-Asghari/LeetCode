# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def dfs(treeNode):
            if not treeNode:
                return 0, 0, None
            
            tiltNode = TreeNode()
            tree_lsum, tilt_lsum, tiltNode.left = dfs(treeNode.left)                
            tree_rsum, tilt_rsum, tiltNode.right = dfs(treeNode.right)
            
            tiltNode.val = abs(tree_lsum - tree_rsum)
            return treeNode.val + tree_lsum + tree_rsum, tiltNode.val + tilt_lsum + tilt_rsum, tiltNode
        
        _, total, _ = dfs(root)
        return total