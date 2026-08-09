# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = {}
        rootCandidates = set()
        children = set()
        
        for parent, child, isLeft in descriptions:
            rootCandidates.add(parent)
            children.add(child)
            
            if parent not in nodeMap:
                nodeMap[parent] = TreeNode(val=parent)
            if child not in nodeMap:
                nodeMap[child] = TreeNode(val=child)
            if isLeft == 1:
                nodeMap[parent].left = nodeMap[child]
            elif isLeft == 0:
                 nodeMap[parent].right = nodeMap[child]
        
        for child in children:
            rootCandidates.discard(child)
        
        rootVal = list(rootCandidates)[0]
        return nodeMap[rootVal]