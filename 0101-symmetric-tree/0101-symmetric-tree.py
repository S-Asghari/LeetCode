# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     in_order_nodes = []
    #     def inOrderTraversal(node):
    #         nonlocal in_order_nodes
    #         if node is not None:
    #             if (node.left is not None) or (node.right is not None):
    #                 inOrderTraversal(node.left)
    #                 in_order_nodes.append(node.val)
    #                 inOrderTraversal(node.right)
    #             else:
    #                 in_order_nodes.append(node.val)
    #         else:
    #             in_order_nodes.append(-101)
        
    #     inOrderTraversal(root)
    #     print(in_order_nodes)
    #     n = len(in_order_nodes) 
    #     if n % 2 != 1:
    #         return False
    #     mid = n // 2
    #     for i in range(mid):
    #         if in_order_nodes[i] != in_order_nodes[n-i-1]:
    #             return False
    #     return True

    # Wrong answer:
    #      5
    #     / \
    #    2   2
    #   /     \
    #  4       1
    #   \       \
    #    1       4
    #   /       /
    #  2       2
        def isMirror(t1, t2):
                if t1 is None and t2 is None:
                    return True
                if t1 is None or t2 is None:
                    return False
                return (t1.val == t2.val
                        and isMirror(t1.left, t2.right)
                        and isMirror(t1.right, t2.left))
            
        return isMirror(root, root)