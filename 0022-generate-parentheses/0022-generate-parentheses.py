from collections import defaultdict

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 1: ()
        # n = 2: (()), ()()
        # n = 3: ((())), (())(), ()(()), (()()), ()()()
        outputs = defaultdict(set)
        outputs[1] = set(["()"]) 
        for i in range(2, n+1):
            for j in range(1, i):
                for s1 in outputs[j]:
                    for s2 in outputs[i-j]:
                        outputs[i].add(s1+s2)
            for s in outputs[i-1]:
                outputs[i].add(f"({s})")
            
        return list(outputs[n])