class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        label = [i for i in range(n)]

        def findLabel(x):
            if x != label[x]:
                return findLabel(label[x])
            return x
        
        def unionLabels(x, y):
            x_label, y_label = findLabel(x), findLabel(y)
            label[x_label] = label[y_label] = min(x_label, y_label)
        
        answer = []
        for x, y in requests:
            x_label, y_label = findLabel(x), findLabel(y)
            canBeFriends = True
            for u, v in restrictions:
                u_label, v_label = findLabel(u), findLabel(v)
                if set([u_label, v_label]) == set([x_label, y_label]):
                    canBeFriends = False
                    break
            answer.append(canBeFriends)
            if canBeFriends:
                unionLabels(x, y)
        
        return answer