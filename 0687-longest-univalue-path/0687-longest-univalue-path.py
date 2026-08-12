# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # Cracking FAANG's Solution
        if not root:
            return 0
        
        res = 0
        
        def DFS(node):
            # return node.val, longest unival path
            nonlocal res
            
            if not node:
                return -1001, 0
            
            if (not node.left) and (not node.right):
                return node.val, 0
            
            l_val, l_longest = DFS(node.left)
            r_val, r_longest = DFS(node.right)

            if node.val == l_val == r_val:
                res = max(
                    res,
                    2 + l_longest + r_longest
                )
                return node.val, 1 + max(l_longest, r_longest)
            
            if node.val == l_val:
                res = max(
                    res,
                    1 + l_longest
                )
                return node.val, 1 + l_longest
            
            elif node.val == r_val:
                res = max(
                    res,
                    1 + r_longest
                )
                return node.val, 1 + r_longest
            
            else:
                return node.val, 0
             
        
        DFS(root)
        return res