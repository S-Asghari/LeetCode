from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    adj[node.val].append(node.left.val)
                    adj[node.left.val].append(node.val)
                    q.append(node.left)
                if node.right:
                    adj[node.val].append(node.right.val)
                    adj[node.right.val].append(node.val)
                    q.append(node.right)
        
        res = []
        visited = set()
        q.append((target.val, 0))
        while q:
            node, dist = q.popleft()
            visited.add(node)
            if dist > k: break
            elif dist == k:
                res.append(node)
                continue
            for nei in adj[node]:
                if nei not in visited:
                    q.append((nei, dist+1))

        return res