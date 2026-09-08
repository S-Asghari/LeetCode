class TrieNode:
    def __init__(self, val: str = "", wc: int = 0):
        self.val = val
        self.wc = wc # word count
        self.children = []
        self.eow = False # end of the word
    
    def __str__(self):
        return f"val: {self.val}, wc: {self.wc}, eow: {self.eow}"

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ----------
        # Solution 1
        # ----------
        # src = strs[0]
        # for i in range(1, len(strs)):
        #     if len(strs[i]) < len(src):
        #         src = strs[i]

        # for j in range(len(src)):
        #     for s in strs:
        #         if s[j] != src[j]:
        #             return src[:j]
        # return src
        # ----------
        # Solution 2
        # ----------
        root = TrieNode()
        
        curNode = root
        for c in strs[0]:
            curNode.children.append(TrieNode(c, 1))
            curNode = curNode.children[0]
        curNode.eow = True

        for s in strs[1:]:
            curNode = root
            for c in s:
                found = False
                for child in curNode.children:
                    if c == child.val:
                        found = True
                        child.wc += 1
                        curNode = child
                        break
                if not found:
                    curNode.children.append(TrieNode(c, 1))
                    curNode = curNode.children[-1]
            curNode.eow = True

        res = ""
        if not root.children: return ""
        
        curNode = root.children[0]
        while curNode.wc == len(strs):
            res += curNode.val
            if curNode.eow or not curNode.children:
                break
            curNode = curNode.children[0]
        
        return res