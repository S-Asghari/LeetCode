# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # NeetCode's Solution!
        valToIdx = {v:i for i, v in enumerate(inorder)}
        
        def helper(l, r):
            if l > r:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            idx = valToIdx[val]
            root.right = helper(idx+1, r)
            root.left = helper(l, idx-1)
            return root

        N = len(inorder)
        return helper(0, N-1)