from collections import defaultdict

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 1: ()
        # n = 2: (()), ()()
        # n = 3: ((())), (())(), ()(()), (()()), ()()()
        # ----------
        # Solution 1
        # ----------
        # outputs = defaultdict(set)
        # outputs[1] = set(["()"]) 
        # for i in range(2, n+1):
        #     for j in range(1, i):
        #         for s1 in outputs[j]:
        #             for s2 in outputs[i-j]:
        #                 outputs[i].add(s1+s2)
        #     for s in outputs[i-1]:
        #         outputs[i].add(f"({s})")
            
        # return list(outputs[n])
        # ----------
        # Solution 2
        # ----------
        res = []
        def backtrack(s, onum, cnum):
            # print(f"s:{s}, onum:{onum}, cnum:{cnum}")
            if onum == n and cnum == n:
                res.append(s)
                return
            
            if onum == cnum:
                backtrack(s+"(", onum+1, cnum)
            elif onum > cnum:
                if onum < n:
                    backtrack(s+"(", onum+1, cnum)
                backtrack(s+")", onum, cnum+1)

        backtrack("", 0, 0)
        return res