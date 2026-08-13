# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        leaves = set()
        for tree in trees:
            if tree.left: leaves.add(tree.left.val)
            if tree.right: leaves.add(tree.right.val)
        
        root = None
        for tree in trees:
            if tree.val not in leaves:
                if root is not None:
                    return None
                else:
                    root = tree
        if not root:
            return None
        
        trees.remove(root)
        treeDict = {}
        for tree in trees:
            treeDict[tree.val] = tree
        
        root = self.helper(root, treeDict)
        if self.checkValidBST(root, 0, 50001) and len(treeDict) == 0: 
            return root
        else:
            return None


    def helper(self, root, treeDict):
        if not root:
            return None
        
        if root.val in treeDict:
            root = treeDict[root.val]
            del treeDict[root.val]
        
        root.left = self.helper(root.left, treeDict)
        root.right = self.helper(root.right, treeDict)
        
        return root


    def checkValidBST(self, root, minLimit, maxLimit):
        if not root:
            return True
        elif minLimit < root.val < maxLimit and \
            self.checkValidBST(root.left, minLimit, root.val) and \
            self.checkValidBST(root.right, root.val, maxLimit):
            return True
        else:
            return False
