# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root: return []
        
        paths = []
        
        def DFS(node, path, s):
            if (not node.left) and (not node.right):
                if s == targetSum:
                    paths.append(path)
                return
            
            if node.left:
                DFS(node.left, path + [node.left.val], s + node.left.val)
            if node.right:
                DFS(node.right, path + [node.right.val], s + node.right.val)


        DFS(root, [root.val], root.val)
        return paths