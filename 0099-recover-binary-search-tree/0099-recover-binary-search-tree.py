# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None
        prevNode = None

        def inOrderTraverse(node):
            nonlocal firstNode, secondNode, prevNode
            if node is not None:
                inOrderTraverse(node.left)
                if (prevNode is not None) and (node.val < prevNode.val) and (firstNode is None):
                    firstNode = prevNode
                if (prevNode is not None) and (node.val < prevNode.val) and (firstNode is not None):
                    secondNode = node

                prevNode = node

                inOrderTraverse(node.right)
        
        inOrderTraverse(root)
        # if (firstNode is not None) and (secondNode is not None):
        firstNode.val, secondNode.val = secondNode.val, firstNode.val