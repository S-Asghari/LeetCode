# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def traverse(node):
            if node:
                res.append(str(node.val))
                traverse(node.left)
                traverse(node.right)
            else:
                res.append("None")

        traverse(root)
        return "[" + ",".join(res) + "]"

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = deque(data[1:-1].split(","))
                
        def buildTree():
            val = vals.popleft()
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = buildTree()
            node.right = buildTree()
            return node
        
        return buildTree()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))