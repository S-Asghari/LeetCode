# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        if root:
            traversal.append(root.val)
            traversal += self.preorderTraversal(root.left)
            traversal += self.preorderTraversal(root.right)
        return traversal