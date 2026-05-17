# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # NeetCode's Solution!
        def helper(l, r):
            if l > r:
                return None
            
            m = (l+r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)

            return root
        
        N = len(nums)
        return helper(0, N-1)
